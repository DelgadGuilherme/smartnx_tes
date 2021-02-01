from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from model.cliente import banco, Cliente
import psycopg2
import json

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from controller import cliente_controller

connection = psycopg2.connect(host='localhost', database='postgres',
user='postgres', password='123')

banco.init_app(app)

if __name__ == '__main__':
    with app.test_request_context():
        banco.create_all()
    app.run(debug=True)