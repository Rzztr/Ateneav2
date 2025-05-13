import os
import sqlite3

SECRET_KEY = '0L1mP0%S3Cr3t'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
DB_PATH = os.path.join(INSTANCE_DIR, '.db')

if not os.path.exists(INSTANCE_DIR):
    os.makedirs(INSTANCE_DIR)

def getDBConn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def initDB():
    with getDBConn() as conn:
        cursor = conn.cursor()
        cursor.execute('''
                        CREATE TABLE IF NOT EXIST users(
                            id INTEGRER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL,
                            nomUser TEXT NOT NULL,
                            apPaterno TEXT NOT NULL
                            apMaterno TEXT NOT NULL
                            numTelefono VARCHAR NOT NULL)''')
        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS ubicaciones (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            latitud REAL NOT NULL,
                            longitud REAL NOT NULL,
                            timestamp TEXT NOT NULL,
                            served BOOLEAN NOT NULL)''')
        conn.commit()
    

initDB()
