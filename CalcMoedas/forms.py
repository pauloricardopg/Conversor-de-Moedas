from flask_wtf import FlaskForm
from wtforms import SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

class Calculo(FlaskForm):
    valor = FloatField('Valor em R$', validators=[DataRequired(), NumberRange(min=0, message="O valor deve ser maior ou igual que 0")], render_kw={"placeholder": "Digite o valor em Reais"})
    botao_calcular = SubmitField('Calcular')