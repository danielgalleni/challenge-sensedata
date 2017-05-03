from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, RadioField
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Tarefa

class FormularioTarefa(FlaskForm):
    """
    Formulario para usuario inserir uma nova tarefa
    """
    tarefa = StringField('Tarefa', validators=[DataRequired()])
    detalhe = StringField('Detalhe', validators=[DataRequired()])
    categoria = RadioField('Categoria', choices=[(1,'Azul'),(2,'Verde'),(3,'Agua'),(4,'Amarela'),(5,'Vermelha')])
    submit = SubmitField('Incluir')

    #def validate_tarefa(self, field):
    #    if field.tarefa.data is None:
    #        raise ValidationError('E necessario informar um nome para a tarefa.')

    #def validate_detalhe(self, field):
    #    if field.detalhe.data is None:
    #        raise ValidationError('E necessario informar um detalhamento para a tarefa.')