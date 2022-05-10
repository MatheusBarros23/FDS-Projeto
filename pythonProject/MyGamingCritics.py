from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import os


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = MySQL(app)

from views import *

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

