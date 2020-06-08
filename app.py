from flask import Flask, render_template, request, session, redirect
import psycopg2
from datetime import date
import random

app = Flask(__name__)

app.secret_key = 'sadkljfsdakljfsdajklfsdlajkklsdjaklhweioyweq34'
app.session_type = 'memcache'
app.debug = True

try:
    conn = psycopg2.connect("host='localhost' dbname='postgres' user='postgres' password='admin'")
except:
    conn = None
    print("Nao bombou a conexao")
# endcatch


@app.route('/')
def index():
    if 'estalogado' in session:
        return render_template("menu.html")
    else:
        return redirect("/login")
    # enddif
# enddef


@app.route('/rota')
def rota():
    return render_template('/index.html')
# enddef


@app.route('/intercepta', methods=['GET', 'POST'])
def intercepta():
    return str(random.randint(10, 100))
# enddef


@app.route('/testescript')
def testescript():
    return render_template('/testescript.html')
# enddef


@app.route('/retorna', methods=['POST'])
def retorna():
    valor = request.form['valor']
    print("o valor recebido eh:", valor)
    return "a vaca morreu pelo retorna da chamada (isso veio da chamada via Jquery)" + str(valor)
# enddef

@app.route('/rota1')
def rota1():
    return render_template('/cadastro.html')
# enddef


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        usuario = usuario.replace("'", '')
        senha = senha.replace("'", '')

        if (conn):
            cur = conn.cursor();
            cur.execute("SELECT nome FROM usuarios WHERE nome = '" + usuario + "' AND senha = '" + senha + "'")
            rows = cur.fetchall()
            if(rows):
                print(rows)
                session['estalogado'] = True
                session['imagem'] = "data:image/jpeg;base64,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"
                session['nome'] = usuario

                print("logou")
            else:
                print(rows)
                session.pop('estalogado', None)
            # endif
        # endif
        return redirect("/")
    # endif
    return render_template("login.html")
# enddef


@app.route('/logout')
def logout():
    session.pop('estalogado', None)
    return redirect("/login")
# enddef


@app.route('/dados')
def dados():
    if(conn):
        cur = conn.cursor();
        cur.execute("SELECT * FROM usuarios")
        rows = cur.fetchall()

        print(rows)

        tabela_dados = "<table border = '1'>"
        tabela_dados += "   <tr>"
        tabela_dados += "      <td>Codigo</td><td>Nome</td><td>Senha</td>"
        tabela_dados += "   </tr>"
        for row in rows:
            tabela_dados += "   <tr>"
            tabela_dados += "      <td>" + str(row[0]) + "</td><td>" + row[1] + "</td><td>" + row[2] + "</td>"
            tabela_dados += "   </tr>"
            print(row)
        tabela_dados += "</table>"
        return tabela_dados
    else:
        return "Sem conexao com o banco de dados"
    # endif
# enddef


# nao executa os comandos abaixo quando estiver usando o pycharm
# porem se executar fora (ou profissionalmente) a linha abaixo sera executada
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# if
