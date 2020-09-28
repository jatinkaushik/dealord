from app import db
from app.v1.user.model import *

class CompanyCompany(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    create_user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))

class CompanyInfo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company_company.id'))
    legal_name = db.Column(db.String(100))
    gstin_no = db.Column(db.String(100))
    cin_no = db.Column(db.String(100))
    website = db.Column(db.String(100))
    email = db.Column(db.String(30))
    phone_no = db.Column(db.String(20))
    fax = db.Column(db.String(30))

class CompanyAddress(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('company_company.id'))
    address_line = db.Column(db.String(100))
    # address_line_2 = db.Column(db.String(100))
    district = db.Column(db.String(30))
    city_town = db.Column(db.String(30))
    landmark = db.Column(db.String(50))
    state = db.Column(db.String(30))
    country = db.Column(db.String(30))
    pin_code = db.Column(db.String(30))


class CompanyUsers(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    company_id = db.Column(db.Integer, db.ForeignKey('company_company.id'))
    

class CompanyRoles(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    display_name = db.Column(db.String(50))
    description = db.Column(db.String(100))

class CompanyRolePermissions(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50))
    permission_name = db.Column(db.String(50))
    description = db.Column(db.String(100))

class PermissionRoleConnect(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    roles_id = db.Column(db.Integer, db.ForeignKey('company_roles.id'))
    permission_id = db.Column(db.Integer, db.ForeignKey('company_role_permissions.id'))

class CompanyRoleUser(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    roles_id = db.Column(db.Integer, db.ForeignKey('company_roles.id'))


