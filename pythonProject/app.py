## Flask, parar criar as rotas da nossa API, Response; para criar o retorno da nossa API, Request; para cadastrar no banco
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/MGC'
db = SQLAlchemy(app)