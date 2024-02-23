# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Avaliação contínua: Aula 030</h1><ul><li><a href="/">Home</a></li><li><a href="/user/Igor_Ramos/PT3019284/IFSP">Identificação</a></li><li><a href="/contextorequisicao">Contexto da requisição</a></li></ul>'

@app.route("/user/Igor_Ramos/PT3019284/IFSP")
def user():
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Aluno: Igor_Ramos</h2><h2>Prontuário: PT3019284</h2><h2>Instituição: IFSP</h2><p><a href="/">Voltar</a></p>'

@app.route("/contextorequisicao")
def context():
    user_agent = request.headers.get('User-Agent')
    url = request.remote_addr
    ip = request.host_url
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {}</h2><h2>O IP do computador remoto é: {}</h2><h2>O host da aplicação é: {}</h2><p><a href="/">Voltar</a></p>'.format(user_agent, url, ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)