from flask import Blueprint
from app.NestedBlueprint import NestedBlueprint

blu_v1 = Blueprint('v1', __name__, url_prefix= '/v1')

from .user import *
from .product import *
from .global_product import *
from .employee import *
# from .countries import *
from .general_data import *
from .company import *
from .customers import *
from .vendors import *
from .items import *