from flask import Flask, request, redirect, render_template, url_for, flash
from flask_mysqldb import MySQL
from flask_session import Session

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

@app.route('/')
def index():
    return redirect(url_for('register'))
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['prénom']
        last_name = request.form['nom de famille']
        email = request.form['Adresse e-mail']
        password = request.form['mot de passe']
        gender = request.form['Genre']
        dob = request.form['dob']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO users (first_name, last_name, email, password, gender, dob) VALUES (%s, %s, %s, %s, %s, %s)", (first_name, last_name, email, password, gender, dob))
        mysql.connection.commit()
        cursor.close()

        flash('Inscription réussie ! Veuillez vous connecter.')
        return redirect('http://127.0.0.1:5007')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5003)
