from flask import Flask, request, redirect, render_template, url_for, flash, jsonify, session, send_file
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from base64 import b64encode, b64decode
import base64
from flask_session import Session  # Importez l'extension Flask Session

app = Flask(__name__)
app.secret_key = "caircocoders-ednalan"

# Configuration de la base de données MySQL
app.config["MYSQL_HOST"] = 'mysqldb'
app.config['MYSQL_USER'] = 'enna'
app.config['MYSQL_PASSWORD'] = 'poiuytre'
app.config['MYSQL_DB'] = 'enameli'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

# Configuration de Flask Session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

app.config['UPLOAD_FOLDER'] = 'static/uploads'

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def execute_sql_file(filename):
    # Lire le contenu du fichier SQL
    with open(filename, 'r') as file:
        sql_file = file.read()

    # Exécuter les commandes SQL dans le fichier
    cursor = mysql.connection.cursor()
    for command in sql_file.split(';'):
        cursor.execute(command)
    mysql.connection.commit()
    cursor.close()

@app.route('/initialize', methods=['GET'])
def initialize_database():
    # Exécuter le fichier SQL pour créer les tables
    execute_sql_file('databases.sql')
    flash('Database initialized successfully!')
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['Adresse e-mail']
        password = request.form['mot de passe']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        cursor.close()

        if user:
            session['user_id'] = user['id']
            session['user_first_name'] = user['first_name']
            
            # Redirigez vers le mur
            return redirect('http://127.0.0.1:5008/wall')
        else:
            flash('E-mail ou mot de passe invalide')
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)