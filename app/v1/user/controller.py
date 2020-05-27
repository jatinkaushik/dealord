import json
import datetime
from app import app
from app.v1.user import User, Token
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
import jwt



def check_token(username, password):
    if check_password_hash(username.password, password):
        token = jwt.encode({'id' : username.id, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=300)}, app.config['SECRET_KEY'])
        return token.decode('UTF-8')
    else:
        return "password_is_incorrect"

def login(auth):
    check_username = User.query.filter_by(username=auth.username).first()
    check_email = User.query.filter_by(email=auth.username).first()
    check_phone = User.query.filter_by(phone=auth.username).first()
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
        check_username = User.query.filter_by(username=json_data['username']).first()
        check_email = User.query.filter_by(email=json_data['email']).first()
        check_phone = User.query.filter_by(phone=json_data['phone']).first()

        if not check_username:
            if not check_email:
                if not check_phone:
                    hashed_password = generate_password_hash(json_data['password'], method='sha256')
                    users_model = User(username=json_data['username'],name=json_data['name'], email=json_data['email'],
                            password=hashed_password, phone=json_data['phone'])
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