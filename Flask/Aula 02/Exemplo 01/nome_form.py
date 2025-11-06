from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NomeForm(FlaskForm):
    nome = StringField('Qual seu nome?', validators=[DataRequired()])
    enviar = SubmitField('Enviar')