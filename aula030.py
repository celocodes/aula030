from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Avaliação contínua: Aula 030</h1><ul><li><a href="/">Home</a></li><li><a href="/user/Marcelo Baldavia/PT3019021/IFSP">Identificação</a></li><li><a href="/contextorequisicao">Contexto de requisição</a></li></ul>'

@app.route('/user/Marcelo Baldavia/PT3019021/IFSP')
def user():
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Aluno: Marcelo Baldavia</h2><h2>Prontuário: PT3019021</h2><h2>Instituição: IFSP</h2><a href="http://127.0.0.1">Voltar</a>'

@app.route('/contextorequisicao')
def contexto():
    user_agent = request.headers.get('User-Agent')
    url = request.host_url
    ip = request.remote_addr
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {}</h2><h2>O IP do computador remoto é: {}</h2><h2>O host da aplicação é: {}</h2><a href="http://127.0.0.1">Voltar</a>'.format(user_agent, ip, url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)