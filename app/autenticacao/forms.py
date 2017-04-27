from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo


from ..models import Pessoa


class FormularioCadastro(FlaskForm):
    """
    Formulario para usuario criar uma nova conta
    """
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    nome_usuario = StringField('Nome de usuario', validators=[DataRequired()])
    nome = StringField('Nome completo', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[
                                        DataRequired(),
                                        EqualTo('confirma_senha')
                                        ])
    confirma_senha = PasswordField('Confirme a senha')
    submit = SubmitField('Registrar')

    def validar_email(self, field):
        if Pessoa.query.filter_by(email=field.data).first():
            raise ValidationError('O e-mail informado pertence a outra conta.')

    def validar_nome_usuario(self, field):
        if Pessoa.query.filter_by(nome_usuario=field.data).first():
            raise ValidationError('O nome de usuario informado ja esta em uso.')


class FormularioLogin(FlaskForm):
    """
    Formulario para usuarios fazerem o login
    """
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Entrar')