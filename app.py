from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey' 


def conectar_banco():
    return sqlite3.connect('banco.db')


@app.route('/')
def home():
    return render_template('site.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        
    
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
        usuario_encontrado = cursor.fetchone()
        
        if usuario_encontrado:
            return redirect(url_for('novidades'))
        else:
            flash('Credenciais inválidas. Tente novamente!', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        email = request.form['email']
        senha = request.form['senha']
        confirmar_senha = request.form['confirmar_senha']
        
        if senha != confirmar_senha:
            flash('As senhas não coincidem. Tente novamente!', 'danger')
            return redirect(url_for('cadastro'))
        
   
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ?", (usuario,))
        usuario_existente = cursor.fetchone()
        
        if usuario_existente:
            flash('Este nome de usuário já está em uso. Escolha outro.', 'danger')
            return redirect(url_for('cadastro'))
        
  
        cursor.execute("INSERT INTO usuarios (usuario, email, senha) VALUES (?, ?, ?)", (usuario, email, senha))
        conexao.commit()
        conexao.close()
        
        flash('Cadastro realizado com sucesso!', 'success')
        return redirect(url_for('login'))

    return render_template('cadastro.html')


@app.route('/novidades')
def novidades():
    return render_template('novidades.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
