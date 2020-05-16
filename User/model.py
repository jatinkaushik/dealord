from flask import Flask, render_template, flash, request, url_for, redirect, session, jsonify
from passlib.hash import sha256_crypt
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask_sqlalchemy import SQLAlchemy
from flask_praetorian import Praetorian
import json
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:bhuvnesh@curesee.in/flask'
app.config['SECRET_KEY'] = 'Dealord'
db = SQLAlchemy(app)
guard = Praetorian(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(1000))
    token_s = db.relationship('Token', backref='user')

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


guard.init_app(app, User)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tokens = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class RegistrationForm(Form):
#     username = TextField('Username', [validators.Length(min=4, max=20)])
#     email = TextField('Email Address', [validators.Length(min=6, max=50)])
#     password = PasswordField('New Password')
#     phone = TextField('Phone No', [validators.Length(min=4, max=15)])


@app.route('/signup', methods=["POST"])
def Registration_page():
    try:
        print(request.json['username'])
        # form = RegistrationForm(request.form)

        # if request.method == 'POST' and form.validate():
        #     username = form.username
        #     email = form.email
        #     password = sha256_crypt.encrypt((str(form.password.data)))
        #     phone = form.phone
        users_model = User(username=request.json['username'], email=request.json['email'],
                           password=sha256_crypt.encrypt(request.json['password']), phone=request.json['phone'])
        check_username = User.query.filter_by(
            username=request.json['username']).first()
        check_email = User.query.filter_by(email=request.json['email']).first()
        check_phone = User.query.filter_by(phone=request.json['phone']).first()

        if not check_username:
            if not check_email:
                if not check_phone:
                    db.session.add(users_model)
                    db.session.commit()
                    return json.dumps("Done")
                else:
                    return json.dumps('phone_exists')
            else:
                return json.dumps('email_exists')
        else:
            return json.dumps('username_exists')
    except:
        return json.dumps('Something Went Wrong')


def check_token(username, password):
    user = guard.authenticate(username, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    user_token = Token(tokens=ret['access_token'], user=user)
    db.session.add(user_token)
    db.session.commit()

    return ret


@app.route('/login', methods=["POST"])
def login_page():
    json_data = request.json
    check_username = User.query.filter_by(
        username=json_data['login']).first()
    check_email = User.query.filter_by(email=json_data['login']).first()
    check_phone = User.query.filter_by(phone=json_data['login']).first()
    # password = sha256_crypt.encrypt(request.json['password'])
    password = json_data['password']
    login_token = {
        "error": "AuthenticationError",
        "message": "The username is incorrect",
        "status_code": 401
    }
    if check_username:
        username = check_username.username
        login_token = check_token(username, password)
    elif check_email:
        username = check_email.username
        login_token = check_token(username, password)
    elif check_phone:
        username = check_phone.username
        login_token = check_token(username, password)

    return json.dumps(login_token)


if __name__ == '__main__':
    app.run(debug=True)
