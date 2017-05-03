from flask import flash
from flask_login import UserMixin
from sqlalchemy import Table, ForeignKey, Integer
from werkzeug.security import generate_password_hash, check_password_hash


from app import banco_dados, gerenciamento_login


class Pessoa(UserMixin, banco_dados.Model):
    """
    Criar a tabela Tarefas
    """

    __tablename__ = 'pessoas'

    id = banco_dados.Column(banco_dados.Integer, primary_key=True)
    email = banco_dados.Column(banco_dados.String(60), index=True, unique=True)
    nome_usuario = banco_dados.Column(banco_dados.String(60), index=True, unique=True)
    nome_completo = banco_dados.Column(banco_dados.String(120), index=True)
    apelido = banco_dados.Column(banco_dados.String(60), index=True)
    senha_hash = banco_dados.Column(banco_dados.String(128))
    #lista_tarefas = banco_dados.Column(Integer, ForeignKey('tarefas.id'))
    #tarefas = banco_dados.relationship('Tarefa', backref='pessoas.id', lazy='dynamic')

    @property
    def senha(self):
        """
        Protege a senha
        """
        raise AttributeError('Nao e permitido saber a senha')

    @senha.setter
    def senha(self, senha):
        """
        Gera o hash da senha
        """
        self.senha_hash = generate_password_hash(senha)

    def verifica_senha(self, senha):
        """
        Verifica se a senha informada esta correta
        """
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return '<Pessoa: {}>'.format(self.nome_usuario)

    def persistir(self):
        # Incluindo cadastro no banco de dados
        try:
            banco_dados.session.add(self)
            banco_dados.session.commit()
            flash('Cadastro realizado com sucesso!  Faca o login para comecar a usar o sistema.')
        except Exception:
            banco_dados.session.ronback()
            flash("Nao foi possivel realizar o seu cadastro. Tente novamente!")

    def atualizar(self):
        # Atualizando cadastro no banco de dados
        try:
            banco_dados.session.put(self)
            banco_dados.session.commit()
            flash('Cadastro atualizado com sucesso!')
        except:
            banco_dados.session.ronback()
            flash("Nao foi possivel atualizar o cadastro.")

    def excluir(self):
        # Excluindo cadastro no banco de dados
        try:
            banco_dados.session.delete(self)
            banco_dados.session.commit()
            flash('Cadastro excluido com sucesso!')
        except Exception:
            banco_dados.session.ronback()
            flash("Nao foi possivel excluir o cadastro.")


# Carregar usuario
@gerenciamento_login.user_loader
def carregar_usuario(id_usuario):
    return Pessoa.query.get(int(id_usuario))


class Tarefa(banco_dados.Model):
    """
    Cria a tabela lista_tarefas
    """

    __tablename__ = 'tarefas'

    id = banco_dados.Column(banco_dados.Integer, primary_key=True)
    tarefa = banco_dados.Column(banco_dados.String(60), index=True)
    detalhe = banco_dados.Column(banco_dados.String(200), index=True)
    categoria = banco_dados.Column(banco_dados.Integer, index=True)

    def __repr__(self):
        return '<Tarefa: {}>'.format(self.tarefa)

    def persistir(self):
        # Incluindo cadastro no banco de dados
        try:
            banco_dados.session.add(self)
            banco_dados.session.commit()
            flash('Tarefa incluida com sucesso!')
        except Exception:
            banco_dados.session.ronback()
            flash("Nao foi possivel incluir a tarefa. Tente novamente!")

    def atualizar(self):
        # Atualizando cadastro no banco de dados
        try:
            banco_dados.session.put(self)
            banco_dados.session.commit()
            flash('Cadastro atualizado com sucesso!')
        except:
            banco_dados.session.ronback()
            flash("Nao foi possivel atualizar o cadastro.")

    def excluir(self):
        # Excluindo cadastro no banco de dados
        try:
            banco_dados.session.delete(self)
            banco_dados.session.commit()
            flash('Cadastro excluido com sucesso!')
        except Exception:
            banco_dados.session.ronback()
            flash("Nao foi possivel excluir o cadastro.")