from passlib.hash import sha256_crypt
from flask_praetorian import Praetorian
import json
import datetime
from app import app
from app.User import User, Token
from app import db

guard = Praetorian(app)
guard.init_app(app, User)

def check_token(username, password):
    user = guard.authenticate(username, password)
    ret = {'access_token': guard.encode_jwt_token(user)}
    user_token = Token(tokens=ret['access_token'], user=user)
    db.session.add(user_token)
    db.session.commit()

    return ret['access_token']

def login(json_data):
    check_username = User.query.filter_by(username=json_data['login']).first()
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
    
    return login_token


def register(json_data):
    try:
        users_model = User(username=json_data['username'], email=json_data['email'],
                           password=sha256_crypt.encrypt(json_data['password']), phone=json_data['phone'])
        check_username = User.query.filter_by(
            username=json_data['username']).first()
        check_email = User.query.filter_by(email=json_data['email']).first()
        check_phone = User.query.filter_by(phone=json_data['phone']).first()

        if not check_username:
            if not check_email:
                if not check_phone:
                    db.session.add(users_model)
                    db.session.commit()
                    return 'Done'
                else:
                    return 'phone_exists'
            else:
                return 'email_exists'
        else:
            return 'username_exists'
    except:
        return 'Something Went Wrong'