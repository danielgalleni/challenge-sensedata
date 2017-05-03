from flask import render_template, url_for
from flask_login import login_required
from werkzeug.utils import redirect

from app.home.forms import FormularioTarefa
from app.models import Tarefa
from . import home

@home.route('/')
def homepage():
    """
    Renderizando o template da pagina inicial no caminho /
    """
    return render_template('home/index.html', title="Seja Bem Vindo", title_painel="Organize o seu dia voce tambem")

@home.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    """
    Inserindo tarefa pelo formulario
    """

    formulario = FormularioTarefa()
    if formulario.validate_on_submit():
        tarefa = Tarefa(tarefa=formulario.tarefa.data(),
                        detalhe=formulario.tarefa.data(),
                        categoria=formulario.tarefa.data())

        tarefa.persistir()

        # TODO: Recaregar aqui a listagem de tarefas utilizando ajax
        return redirect(url_for('home.dashboard'))

    # Renderizando o template da pagina inicial no caminho /dashboard
    return render_template('home/dashboard.html', title="Cadastro", form=formulario, title_painel="Cadastre sua tarefa")
