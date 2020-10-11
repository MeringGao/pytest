from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, relationship

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/flask'

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'tb_user'
    id = Column(Integer, primary_key=True)
    username = db.Column(String(80))

    email = Column(String(120), unique=True)

    def __repr__(self):
        return f'<User {self.username}>'


class Address(db.Model):
    __tablename__ = 'tb_address'

    user = db.relationship('User', backref=db.backref('addresses', lazy=True))

    user_id = Column(Integer, ForeignKey('tb_user.id'))
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
