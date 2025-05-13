from harpo import *
from flask import Flask, request, session, render_template, redirect, url_for, jsonify
from datetime import datetime
#Make dir of each user from Harpo class
def HarpoDirs():
    username = "RELC040721HASYPHA4"
    password = '1234532'
    cypher = Harpo(nomUsuario=username, passUser=password)
    cypher.mkdiruser()
    cypher.hashPassword(password)

app = Flask(__name__)
app.secret_key = 'D4Rk_v1P3r'

app.register_blueprint()