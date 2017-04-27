from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user


from . import autenticacao
from forms import FormularioLogin, FormularioCadastro
from .. import banco_dados
from ..models import Pessoa


@autenticacao.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    """
    Incluir uma pessoa atraves do formulario de cadastro 
    """

    formulario = FormularioCadastro()
    if formulario.validate_on_submit():
        pessoa = Pessoa(email=formulario.email.data,
                        nome_usuario=formulario.nome_usuario.data,
                        nome=formulario.nome.data,
                        senha=formulario.senha)

        pessoa.persistir()

        flash("Cadastro realizado com sucesso!  Faca o login para comecar a usar o sistema.")

        # Redirecionando para papagina de login/autenticacao
        return redirect(url_for("autenticacao.entrar"))


    # Carregando a pagina de cadastro
    return render_template("autenticacao/cadastro.html", formulario=formulario, title="Cadastro")

@autenticacao.route("/entrar", methods=["GET", "Post"])
def entrar():
    """
    Entrar no sistema atraves do formulario de login 
    """

    formulario = FormularioLogin()
    if formulario.validate_on_submit():

        # Verificar se os dados de login informados existem na base de dados
        pessoa = Pessoa.query.filter_by(email=formulario.email.data).first()
        if pessoa is not None and pessoa.verifica_senha(formulario.senha.data):

            # Autenticando o usuario
            login_user(pessoa)

            # Redirecionando para o dashboard
            return redirect(url_for("home.dashboard"))

        # Para usuario ou senha invalidos
        else:
            flash("Nome de usuario ou senha invalidos.")

    # Carregando a pagina de login
    return render_template("autenticacao/entrar.html", formulario=formulario, title="Login")

@autenticacao.route("/sair")
@login_required
def sair():
    """
    Sair do sistema
    """

    logout_user()
    flash("Voce saiu do sistema.")

    # Redirecionando para a pagina de login
    return redirect(url_for("autenticacao.entrar"))