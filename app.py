from flask import Flask, render_template, request, session, redirect
import psycopg2
from datetime import date

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
