from flask import Flask, render_template, request, session, redirect
from datetime import date

app = Flask(__name__)
app.secret_key = 'sadkljfsdakljfsdajklfsdlajkklsdjaklhweioyweq34'


@app.route('/')
def index():
    if 'estalogado' in session:
        return render_template("menu.html")
    else:
        return redirect("/login")
    # enddif
# enddef


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if (usuario == 'admin' and senha == 'admin'):
            session['estalogado'] = True
        # endif

        return redirect("/")
    # endif
    return render_template("login.html")
# enddef


@app.route('/logout')
def logout():
    session.pop('estalogado', None)
    return redirect("/login")


@app.route('/dados')
def dados():
    return ""


# nao executa os comandos abaixo quando estiver usando o pycharm
# porem se executar fora (ou profissionalmente) a linha abaixo sera executada
if __name__ == '__main__':
    app.secret_key = 'sadkljfsdakljfsdajklfsdlajkklsdjaklhweioyweq34'
    app.session_type = 'memcache'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
