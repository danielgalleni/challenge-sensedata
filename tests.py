import unittest
import os
from flask import abort, url_for
from flask_testing import TestCase


from app import create_app, banco_dados
from app.models import Pessoa, Tarefa


class TesteBasico(TestCase):

    def create_app(self):

        # Ajustando configuracao para teste
        config_name = 'testing'
        app = create_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql://teste:teste@localhost/sensedata_teste'
        )

        return app

    def setUp(self):
        """
        Executado antes de todos os testes
        """

        banco_dados.create_all()

        # Criando usuario de teste
        pessoa1 = Pessoa(nome_usuario="usuario_teste", senha="teste123")
        pessoa2 = Pessoa(nome_usuario="teste_usuario", senha="123teste")

        # Persistindo usuario no banco de dados
        banco_dados.session.add(pessoa1)
        banco_dados.session.add(pessoa2)
        banco_dados.session.commit()

    def tearDown(self):
        """
        Executado depois de todos os testes
        """

        banco_dados.session.remove()
        banco_dados.drop_all()


class TesteModels(TesteBasico):

    def teste_pessoa_model(self):
        """
        Teste o numero de registros na tabela pessoas
        """

        self.assertEqual(Pessoa.query.count(), 2)

    def teste_tarefa_model(self):
        """
        Testa o numero de registros na tabela tarefas 
        """

        # Inserindo tarefas de teste
        tarefa1 = Tarefa(tarefa="Testar TODO List", detalhe="Testar primeira linha de cadastro da tarefa", categoria=1)
        tarefa2 = Tarefa(tarefa="TODO List Clean", detalhe="Limpar dados de teste do TODO List", categoria=1)

        # Persistindo dados na tabela tarefas
        banco_dados.session.add(tarefa1)
        banco_dados.session.add(tarefa2)
        banco_dados.session.commit()

        self.assertEqual(Tarefa.query.count(), 2)

class TesteViews(TesteBasico):

    def teste_home_view(self):
        """
        Testa acessibilidade da homepage sem o usuario estar logado
        """

        response = self.client.get(url_for("home.homepage"))
        self.assertEqual(response.status_code, 200)


    def teste_entrar_view(self):
        """
        Testa acessibilidade da pagina de login sem o usuario estar logado
        """

        response = self.client.get(url_for("autenticacao.entrar"))
        self.assertEqual(response.status_code, 200)


    def teste_sair_view(self):
        """
        Testa acessibilidade da pagina de logout sem o usuario estar logado
        e direciona para a tela de login e depois volta para logout
        """

        url_destino = url_for("autenticacao.sair")
        url_redirecionamento = url_for("autenticacao.entrar", next=url_destino)
        response = self.client.get(url_destino)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url_redirecionamento)

        response = self.client.get(url_for("autenticacao.entrar"))
        self.assertEqual(response.status_code, 200)


    def teste_dashboard_view(self):
        """
        Testa acessibilidade da pagina de dashboard sem o usuario estar logado
        e direciona para a tela de login e depois volta para dashboard
        """

        url_destino = url_for("home.dashboard")
        url_redirecionamento = url_for("autenticacao.entrar", next=url_destino)
        response = self.client.get(url_destino)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, url_redirecionamento)

        response = self.client.get(url_for("autenticacao.entrar"))
        self.assertEqual(response.status_code, 200)


class TesteErrosPagina(TesteBasico):

    def testar_erro_403(self):
        """
        Cria rota para forcar o erro 403
        """

        @self.app.route("/403")
        def erro_403():
            abort(403)

        response = self.client.get("/403")
        self.assertEqual(response.status_code, 403)
        self.assertTrue("Erro 403" in response.data)


    def testar_erro_404(self):
        response = self.client.get("/endereco-invalido")
        self.assertEqual(response.status_code, 404)
        self.assertTrue("Erro 404" in response.data)


    def testar_erro_500(self):
        """
        Cria rota para forcar o erro 500
        """

        @self.app.route("/500")
        def erro_500():
            abort(500)

        response = self.client.get("/500")
        self.assertEqual(response.status_code, 500)
        self.assertTrue("Erro 500" in response.data)


class TestaCRUD(TesteBasico):
    """
    Teste todas as opcoes do CRUD
    """

    def testar_cadastrar_pessoa(self):

        # Inserir cadastro de pessoa
        pessoa = Pessoa(
            email="teste@mail.com.br",
            nome_usuario="testemail",
            nome="Teste Mail",
            apelido="Testinho",
            senha="Teste123"
        )

        pessoa.persistir()

        self.assertGreater(pessoa.id, 0)


    def testar_excluir_pessoa(self):
        pessoa = Pessoa.query.filter_by(nome_usuario="usuario_teste").first()
        pessoa.excluir()
        self._baseAssertEqual()




if __name__ == '__main__':
    unittest.main()