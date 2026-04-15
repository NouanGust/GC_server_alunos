from flask import Flask, render_template, request, redirect, send_from_directory, session
import os
import socket
import sqlite3


# Inicialização do Flask
app = Flask(__name__)
app.secret_key = '63f4945d921d599f27ae4fdf5bada3f1'

# Constantes e configurações iniciais
BASE_UPLOAD_FOLDER = 'Cursos'

CURSOS_DISPONIVEIS = ['Game2D', 'Python']

for curso in CURSOS_DISPONIVEIS:
    caminho = os.path.join(BASE_UPLOAD_FOLDER, curso)
    if not os.path.exists(caminho):
        os.makedirs(caminho)

DB_NAME = 'GC_database'


# Banco de dados
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn
    
def init_db():
    conn = get_connection()
    conn.execute('''
                 CREATE TABLE IF NOT EXISTS usuarios(
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT UNIQUE NOT NULL,
                     senha TEXT NOT NULL,
                     role TEXT NOT NULL,
                     curso TEXT
                 )
                 ''')
    cursor = conn.execute('SELECT * FROM usuarios WHERE role = "professor"')
    if not cursor.fetchone():
        conn.execute('INSERT INTO usuarios (username, senha, role, curso) VALUES (?, ?, ?, ?)', ('professor', '123', 'professor', 'todos'))
        conn.execute('INSERT INTO usuarios (username, senha, role, curso) VALUES (?, ?, ?, ?)',('teste', 'abc', 'aluno', 'python' ))
        conn.commit()
    conn.close()
    
init_db()


# Rotas e funções       
        
@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['usuario']
        senha = request.form['senha']
        
        # Busca no DB por usuarios
        conn = get_connection()
        usuario_db = conn.execute("SELECT * FROM usuarios WHERE username = ? AND senha = ?", (user, senha)).fetchone()
        conn.close()
        
        if usuario_db:
            session['usuario'] = user
            session['role'] = usuario_db['role']
            session['curso'] = usuario_db['curso']
            return redirect('/')
        else:
            error = "Usuário ou senha incorretos!"

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


@app.route('/')
def index():
    if 'usuario' not in session:
        return redirect('/login')

    arquivos_por_curso = {}
    
    if session['role'] == 'professor':
        for curso in CURSOS_DISPONIVEIS:
            arquivos_por_curso[curso] = os.listdir(os.path.join(BASE_UPLOAD_FOLDER, curso))
    else:
        meu_curso = session['curso']
        arquivos_por_curso[meu_curso] = os.listdir(os.path.join(BASE_UPLOAD_FOLDER, meu_curso))

    return render_template('dashboard.html', arquivos_por_curso=arquivos_por_curso, cursos_disponiveis=CURSOS_DISPONIVEIS)


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'usuario' not in session or session['role'] != 'professor':
        return "Acesso Negado", 403
    
    curso_destino = request.form.get('curso_destino')
    file = request.files.get('file')
    
    if file and file.filename != '' and curso_destino in CURSOS_DISPONIVEIS:
        caminho_salvar = os.path.join(BASE_UPLOAD_FOLDER, curso_destino, file.filename)
        file.save(caminho_salvar)
    return redirect('/')


@app.route('/cadastrar_aluno', methods=['POST'])
def cadastrar_aluno():
    if 'usuario' not in session or session['role'] != 'professor':
        return "Acesso Negado", 403
    
    novo_user = request.form.get('novo_usuario')
    nova_senha = request.form.get('nova_senha')
    curso_aluno = request.form.get('curso_aluno')
    
    conn = get_connection()
    try:
        conn.execute('INSERT INTO usuarios (username, senha, role, curso) VALUES(?, ?, ?, ?)', (novo_user, nova_senha, 'aluno', curso_aluno))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()
    return redirect('/')
    

@app.route('/download/<curso>/<filename>')
def download_file(curso, filename):
    if 'usuario' not in session:
        return redirect('/login')
    
    if session['role'] != 'professor' and session['curso'] != curso:
        return "Acesso Negado: Essa não é sua turma!", 403


    pasta_do_arquivo = (os.path.join(BASE_UPLOAD_FOLDER, curso))
    return send_from_directory(pasta_do_arquivo, filename, as_attachment=True)


# DEBUG 

def descobrir_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

if __name__ == '__main__':
    print(f"Servidor rodando em: http://{descobrir_ip()}:5000")
    app.run(host='0.0.0.0', port=5000)