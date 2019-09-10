from app import db


class TipoUsuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(256))
    usuarios = db.relationship('Usuario', backref='tipo', lazy=True)

    def __repr__(self):
        return "<TipoUsuario '{:s}'>".format(self.descricao)
