from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

class ClienteForm(FlaskForm):
    nome = StringField(
        "Nome completo",
        validators=[
            DataRequired(message="Por favor, insira o nome completo."),
            Length(min=3, max=50, message="O nome deve ter entre 3 e 50 caracteres.")
        ]
    )

    email = EmailField(
        "E-mail",
        validators=[
            DataRequired(message="Por favor, insira um endereço de e-mail."),
            Email(message="Por favor, insira um e-mail válido (ex: nome@dominio.com).")
        ]
    )

    telefone = StringField(
        "Telefone",
        validators=[
            DataRequired(message="Por favor, insira o telefone."),
            Regexp(
                r'^\(?\d{2}\)?[\s-]?\d{4,5}[\s-]?\d{4}$',
                message="Telefone inválido. Use o formato (XX) XXXXX-XXXX."
            )
        ]
    )

    submit = SubmitField("Cadastrar")
