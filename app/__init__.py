from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
# from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# import NestedBlueprint



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:bhuvnesh@curesee.in/flask'
app.config['SECRET_KEY'] = 'Dealord'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

# blu_api = Blueprint('api', __name__, url_prefix= '/api')

migrate = Migrate(app,db)

from app.v1 import *
# from app.User.route import blu_user
# from .token_required import token_required
app.register_blueprint(blu_v1)