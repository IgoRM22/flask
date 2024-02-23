# A very simple Flask Hello World app for you to get started with...
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>Teste!</p><table><tr><td><b>Aluno:</b></td><td>Igor Ramos Almeida</td></tr><tr><td><b>Prontuário:</b></td><td>PT3019284</td></tr></table>'
