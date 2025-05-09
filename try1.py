from flask import Flask
from flask_hashing import Hashing

app = Flask(__name__)
hashing = Hashing(app)

h = hashing.hash_value('secretdata', salt='abcd')
if hashing.check_value(h, 'secretdata', salt='abcd'):
    print('lol')
else: 
    print('no')