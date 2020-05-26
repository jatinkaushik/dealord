from flask import Blueprint
from app.NestedBlueprint import NestedBlueprint

blu_v1 = Blueprint('v1', __name__, url_prefix= '/v1')

from .user import *
from .product import *