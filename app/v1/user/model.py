from app import db
from app.v1.product import *
from app.v1.global_product import *

class UserUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(1000))
    token_rel = db.relationship('UserToken', backref='user_user')
    category_rel = db.relationship('Category', backref='user_user')
    name=db.Column(db.String(50))
    category_global_rel = db.relationship('GlobalProductCategory', backref='user_user')


    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    # def is_valid(self):
    #     return self.is_active




class UserToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tokens = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    created_at = db.Column(db.DateTime)

# class RegistrationForm(Form):
#     username = TextField('UserUsername', [validators.Length(min=4, max=20)])
#     email = TextField('Email Address', [validators.Length(min=6, max=50)])
#     password = PasswordField('New Password')
#     phone = TextField('Phone No', [validators.Length(min=4, max=15)])
