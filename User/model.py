from flask import Flask, render_template, flash, request, url_for, redirect, session
from passlib.hash import sha256_crypt
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:bhuvnesh@curesee.in/flask'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(1000))


# class RegistrationForm(Form):
#     username = TextField('Username', [validators.Length(min=4, max=20)])
#     email = TextField('Email Address', [validators.Length(min=6, max=50)])
#     password = PasswordField('New Password')
#     phone = TextField('Phone No', [validators.Length(min=4, max=15)])


@app.route('/', methods=["POST"])
def Registration_page():
    # try:
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
    # except:
    return json.dumps('Something Went Wrong')


if __name__ == '__main__':
    app.run(debug=True)
