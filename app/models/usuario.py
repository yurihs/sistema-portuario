from flask_login import UserMixin

from app import db, login_manager


class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(256))
    email = db.Column(db.String(256), index=True)
    hash_senha = db.Column(db.String(256))


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

