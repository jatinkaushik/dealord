import json
import datetime
from app import app
from app.v1.user import UserUser, UserToken
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask import make_response



def check_token(user, password):
    if check_password_hash(user.password, password):
        token = jwt.encode({'id' : user.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=300)}, app.config['SECRET_KEY'])
        return token.decode('UTF-8')
    else:
        return "password_is_incorrect"

def login(auth):
    check_username = UserUser.query.filter_by(username=auth.username).first()
    check_email = UserUser.query.filter_by(email=auth.username).first()
    check_phone = UserUser.query.filter_by(phone=auth.username).first()
    password = auth.password

    if check_username:
        username = check_username.username
        token = check_token(check_username, password)
    elif check_email:
        username = check_email.username
        token = check_token(check_email, password)
    elif check_phone:
        username = check_phone.username
        token = check_token(check_phone, password)
    else:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})
    
    return json.dumps({'token' : token})



def register(json_data):
    try:
        check_username = UserUser.query.filter_by(username=json_data['username']).first()
        check_email = UserUser.query.filter_by(email=json_data['email']).first()
        check_phone = UserUser.query.filter_by(phone=json_data['phone']).first()

        if not check_username:
            if not check_email:
                if not check_phone:
                    hashed_password = generate_password_hash(json_data['password'], method='sha256')
                    users_model = UserUser(username=json_data['username'],name=json_data['name'], email=json_data['email'],
                            password=hashed_password, phone=json_data['phone'])
                    db.session.add(users_model)
                    db.session.commit()
                    token = check_token(users_model, json_data['password'])
                    return {'token' : token}
                else:
                    return 'phone_exists'
            else:
                return 'email_exists'
        else:
            return 'username_exists'   
    except:
        return 'Something Went Wrong'

def user_info(current_user):
    user = {}
    user["id"] = current_user.id
    user["name"] = current_user.name
    user["email"] = current_user.email
    return user