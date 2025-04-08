from flask import render_template, request
from CalcMoedas.forms import Calculo
from CalcMoedas import app
import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()

@app.route('/', methods=['GET', 'POST'])
def dolar():
    calculo_form =  Calculo()
    resultado = None
    
    if calculo_form.validate_on_submit() and 'botao_calcular' in request.form:
        valor = calculo_form.valor.data
        valor_cotacao = float(cotacoes_dic['USD']['bid'])
        resultado =  valor / valor_cotacao
    


    return render_template('dolar.html',calculo_form=calculo_form, resultado=resultado)

@app.route('/euro', methods=['GET', 'POST'])
def euro():
    calculo_form =  Calculo()
    resultado = None

    if calculo_form.validate_on_submit() and 'botao_calcular' in request.form:
        valor = calculo_form.valor.data
        valor_cotacao = float(cotacoes_dic['EUR']['bid'])
        resultado =  valor / valor_cotacao
        


    return render_template('euro.html',calculo_form=calculo_form, resultado=resultado)

@app.route('/Bitcoin', methods=['GET', 'POST'])
def bitcoin():
    calculo_form =  Calculo()
    resultado = None

    if calculo_form.validate_on_submit() and 'botao_calcular' in request.form:
        valor = calculo_form.valor.data
        valor_cotacao = float(cotacoes_dic['BTC']['bid'])
        resultado =  valor /valor_cotacao
    


    return render_template('bitcoin.html',calculo_form=calculo_form, resultado=resultado)