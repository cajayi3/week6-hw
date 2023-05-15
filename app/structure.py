from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Structure):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))

    def __repr__(self):
        return f'User: {self.username}'

    def commit(self):
        db.session.add(self)
        db.session.commit()
        db.session.commit()

    def hash_password(self,password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)