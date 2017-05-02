from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
def homepage():
    """
    Renderizando o template da pagina inicial no caminho /
    """
    return render_template('home/index.html', title="Seja Bem Vindo", title_painel="Organize o seu dia voce tambem")

@home.route('/dashboard')
#@login_required
@login_required
def dashboard():
    """
    Renderizando o template da pagina inicial no caminho /dashboard
    """
    return render_template('home/dashboard.html', title="Cadastro", title_painel="Cadastre sua tarefa")
