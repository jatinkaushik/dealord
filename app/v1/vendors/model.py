from app import db
from app.v1.company.model import *

class VendorsVendor(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    company_id = db.Column(db.Integer,db.ForeignKey('company_company.id'))

class VendorsAddress(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors_vendor.id'))
    address_line_1 = db.Column(db.String(100))
    address_line_2 = db.Column(db.String(100))
    district = db.Column(db.String(30))
    city_town = db.Column(db.String(30))
    landmark = db.Column(db.String(50))
    state = db.Column(db.String(30))
    country = db.Column(db.String(30))
    pin_code = db.Column(db.String(30))

class VendorsInfo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors_vendor.id'))
    legal_name = db.Column(db.String(100))
    gstin_no = db.Column(db.String(100))
    cin_no = db.Column(db.String(100))
    website = db.Column(db.String(100))
    email = db.Column(db.String(30))
    phone_no = db.Column(db.String(20))
    fax = db.Column(db.String(30))