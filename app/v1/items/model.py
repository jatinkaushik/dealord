from app import db
from app.v1.company.model import *

class ItemsProduct(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    active = db.Column(db.Boolean)
    description_of_products = db.Column(db.String(2000)) 
    company_id = db.Column(db.Integer,db.ForeignKey('company_company.id'))