from flask import abort, Flask, render_template
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os


from config import app_config


# Inicializando variavel para p banco de dados
banco_dados = SQLAlchemy()
gerenciamento_login = LoginManager()


def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_object(app_config[config_name])
        app.config.from_pyfile("/home/daniel/Documents/challenge-sensedata/instance/config.py")


    Bootstrap(app)
    banco_dados.init_app(app)
    gerenciamento_login.init_app(app)
    gerenciamento_login.login_message = "Voce precisa fazer login para acessar sua lista de tarefas"
    gerenciamento_login.login_view = "autenticacao.entrar"
    migrate = Migrate(app, banco_dados)

    from app import models

    from .autenticacao import autenticacao as autenticacao_blueprint
    app.register_blueprint(autenticacao_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(erro):
        return render_template("erros/403.html", title="Erro 403", title_painel="Erro! Acesso proibido"), 403

    @app.errorhandler(404)
    def page_not_found(erro):
        return render_template('erros/404.html', title='Erro 404', title_painel="Erro! Pagina nao encontrada"), 404

    @app.errorhandler(500)
    def internal_server_error(erro):
        return render_template('erros/500.html', title='Erro 500', title_painel="Erro! Algo deu errado :/"), 500

    return app