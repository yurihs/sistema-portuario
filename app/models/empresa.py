from app import db


class Empresa(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	nome_fantasia = db.Column(db.String(256))
	razao_social = db.Column(db.String(256))
	cnpj = db.Column(db.String(14), unique=True)
	email = db.Column(db.String(256), unique=True)
	telefone = db.Column(db.String(100))
	endereco = db.Column(db.String(256))
	cidade = db.Column(db.String(256))
	estado = db.Column(db.String(256))