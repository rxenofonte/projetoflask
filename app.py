from flask import Flask, render_template
import pandas as pd

tabela= pd.read_csv("ibge_populacao.csv", sep=",")

usuarios = []
usuarios.append({"nome":"Rommel Teles","email":"r@gmail.com","idade":41})
usuarios.append({"nome":"Rodrigo Teles","email":"rx@gmail.com","idade":43})
usuarios.append({"nome":"Ana Barreto","email":"ax@gmail.com","idade":60})
usuarios.append({"nome":"David Xenofonte","email":"dm@gmail.com","idade":4})
usuarios.append({"nome":"Diego Xenofonte","email":"dx@gmail.com","idade":15})

def pop_fortaleza():
    populacao = int(tabela.query('ano==2021&sigla_uf=="CE"&id_municipio==2304400').populacao)
    return {"populacao":populacao}

def pop_ceara():
    populacao = int(tabela.query('ano==2021&sigla_uf=="CE"').populacao.sum())
    return {"populacao":populacao}

def usuario(nome:str,tipo:int):
    retorno = 'Usuario não existe'

    for i in usuarios:
        if i["nome"] == nome:
            if tipo == '1':
                retorno = str(i["idade"])
            else:
                retorno = str(i["email"])
            break
 
    return retorno

def usuario2(dado:str):
    retorno = 'Usuario não existe'

    for i in usuarios:
        if i["nome"] == dado or i["email"] == dado:
            retorno = i
            break
 
    return retorno


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