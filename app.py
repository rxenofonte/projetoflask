from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/contato')
def contato():
    return render_template('contato.html')
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

app.run(debug=True)