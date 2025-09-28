import os
from flask import Flask, render_template

# Criação do app Flask
app = Flask(__name__)

# Chave secreta para sessões
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'uma_chave_de_dev_aleatoria')

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página "Sobre"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rodando a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
