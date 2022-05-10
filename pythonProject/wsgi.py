from flask import Flask
from flask_mysqldb import MySQL

from helpers import *


app.config.from_pyfile('config.py')
db = MySQL(app)
app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True)