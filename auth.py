from flask import Blueprint, request, session, render_template, redirect, url_for
from config import getDBConn
import sqlite3

auth_bd = Blueprint('auth', __name__)

@auth_bd.route('/login', methods=['GET', 'POST'])

class auth:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    '''

    def login(username, password):
        if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not username or not password:
            return "faltan datos de inicio de sesion", 400

        with getDBConn() as conn: 
            cursor = conn.cursor()
            cursor.execute("SELECT username, password, FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
#TODO Terminar modulo de logim, registro y consultas en clase auth y en models
        if user and user['password'] == password:
            session['username'] = username
            return redirect(url_for(''))
    
    '''
