from flask_sqlalchemy import SQLAlchemy
import psycopg2

banco = SQLAlchemy()

class Cliente(banco.Model):
    codigo = banco.Column('codigo', banco.Integer, primary_key=True, autoincrement=True)
    nome = banco.Column(banco.String(80))
    razao_social = banco.Column(banco.String(50))
    cnpj = banco.Column(banco.String(20))
    data_inclusao = banco.Column(banco.String(15))

    def __init__(self, nome, razao_social, cnpj, data_inclusao):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.data_inclusao = data_inclusao

    def to_dict(self, columns=[]):
        if not columns:
            return{
                'codigo' : self.codigo,
                'nome' : self.nome,
                'razao_social' : self.razao_social,
                'cnpj' : self.cnpj,
                'data_inclusao' : str(self.data_inclusao)
            }
        else:
            return{col: getattr(self, col) for col in columns}