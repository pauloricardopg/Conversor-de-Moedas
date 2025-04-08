from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = '46ca2defb01cc7f0b122f36e6ca22e8q'

from CalcMoedas import routes