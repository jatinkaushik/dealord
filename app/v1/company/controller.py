import json
from app import app, db
from app.v1.company.model import *

def create_company(current_user, json_data):
    # try:
        
        company_model = CompanyCompany(name=json_data['name'], create_user_id=current_user.id) 
        db.session.add(company_model)
        db.session.commit()
        if 'company_info' in json_data:
            info = company_info(json_data['company_info'],company_model.id)
        if 'company_address' in json_data:
            address = company_address(json_data['company_address'],company_model.id)
        return "done"

    # except:
    #     return 'Something Went Wrong'

def fetch_company(company_id):
    try:
        fetch_company = CompanyCompany.query.filter_by(id=company_id).first()
        obj = {
                "id": fetch_company.id,
                "name": fetch_company.name,
                "user_id":fetch_company.create_user_id
                
            }
        return obj
    except:
        return 'Something Went Wrong'

# def fetch_company(country_id):
#     try:
#         fetch_user = 

def company_info(json_data,company_id):
    try:
        legal_name, gstin_no, cin_no, website,email,phone_no,fax = None,None,None,None,None,None,None
        if('legal_name' in  json_data and json_data['legal_name'] != None):
            legal_name = json_data['legal_name']
        if('gstin_no' in  json_data and json_data['gstin_no'] != None):
            gstin_no = json_data['gstin_no']
        if('cin_no' in  json_data and json_data['cin_no'] != None):
            cin_no = json_data['cin_no']
        if('website' in  json_data and json_data['website'] != None):
            website = json_data['website']
        if('email' in  json_data and json_data['email'] != None):
            email = json_data['email']
        if('phone_no' in  json_data and json_data['phone_no'] != None):
            phone_no = json_data['phone_no']
        if('fax' in  json_data and json_data['fax'] != None):
            fax = json_data['fax']
        country_info_obj = CompanyInfo(
            company_id= company_id,
            legal_name = legal_name,
            gstin_no = gstin_no,
            cin_no = cin_no,
            website = website,
            email = email,
            phone_no = phone_no,
            fax = fax) 
        db.session.add(country_info_obj)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_company_info(company_id):
    try:
        fetch_company_info = CompanyInfo.query.filter_by(company_id=company_id).first()
        obj = {
                "id": fetch_company_info.id,
                "company_id":fetch_company_info.company_id,
                "legal_name":fetch_company_info.legal_name,
                "gstin_no":fetch_company_info.gstin_no,
                "cin_no":fetch_company_info.cin_no,
                "website":fetch_company_info.website,
                "email":fetch_company_info.email,
                "phone_no":fetch_company_info.phone_no,
                "fax":fetch_company_info.fax
                
            }
        return obj
    except:
        return 'Something Went Wrong'

def company_address(json_data,company_id):
    address_line, district, city_town, landmark,pin_code,state,country = None,None,None,None,None,None,None
    if('address_line' in  json_data and json_data['address_line'] != None):
        address_line = json_data['address_line']
    if('district' in  json_data and json_data['district'] != None):
        district = json_data['district']
    if('city_town' in  json_data and json_data['city_town'] != None):
        city_town = json_data['city_town']
    if('landmark' in  json_data and json_data['landmark'] != None):
        landmark = json_data['landmark']
    if('pin_code' in  json_data and json_data['pin_code'] != None):
        pin_code = json_data['pin_code']
    if('state' in  json_data and json_data['state'] != None):
        state = json_data['state']
    if('country' in  json_data and json_data['country'] != None):
        country = json_data['country']
    try:
        company_address_obj = CompanyAddress(
            company_id= company_id,
            address_line = address_line,
            district = district,
            city_town = city_town,
            landmark = landmark,
            state = state,
            country = country,
            pin_code = pin_code)
        db.session.add(company_address_obj)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_company_address(company_id):
    try:
        fetch_company_address = CompanyAddress.query.filter_by(company_id=company_id).first()
        obj = {
                "id": fetch_company_address.id,
                "company_id":fetch_company_address.company_id,
                "address_line_1":fetch_company_address.address_line_1,
                "address_line_2":fetch_company_address.address_line_2,
                "district":fetch_company_address.district,
                "city_town":fetch_company_address.city_town,
                "landmark":fetch_company_address.landmark,
                "state":fetch_company_address.state,
                "country":fetch_company_address.country,
                "pin_code":fetch_company_address.pin_code
                
            }
        return obj
    except:
        return 'Something Went Wrong'

def fetch_all_company_info(company_id):
    try:
        fetch_company = CompanyCompany.query.filter_by(id=company_id).first()
        fetch_company_info = CompanyInfo.query.filter_by(company_id=company_id).first()
        fetch_company_address = CompanyAddress.query.filter_by(company_id=company_id).first()
        company_data = {
            "company" :[],
            "company_info":[],
            "company_address":[]
        }
        obj1 ={
                "id": fetch_company.id,
                "name": fetch_company.name,
                "user_id":fetch_company.create_user_id
            }
        obj2 ={
                "id": fetch_company_info.id,
                "legal_name":fetch_company_info.legal_name,
                "gstin_no":fetch_company_info.gstin_no,
                "cin_no":fetch_company_info.cin_no,
                "website":fetch_company_info.website,
                "email":fetch_company_info.email,
                "phone_no":fetch_company_info.phone_no,
                "fax":fetch_company_info.fax
            }
        obj3 = {
                "id": fetch_company_address.id,
                "address_line_1":fetch_company_address.address_line,
                "district":fetch_company_address.district,
                "city_town":fetch_company_address.city_town,
                "landmark":fetch_company_address.landmark,
                "state":fetch_company_address.state,
                "country":fetch_company_address.country,
                "pin_code":fetch_company_address.pin_code
            }
        company_data["company"].append(obj1)
        company_data["company_info"].append(obj2)
        company_data["company_address"].append(obj3)
        return company_data
    except:
        return 'Something Went Wrong'

def add_company_permission(json_data):
    try:
        add_permission = CompanyRolePermissions(name = json_data['name'],permission_name = json_data['permission_name'],description = json_data['description'])
        db.session.add(add_permission)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def edit_company_permission(json_data):
    try:
        edit_permission = CompanyRolePermissions.query.filter_by(id=json_data['id']).first()
        if 'name' in json_data:
            edit_permission.name = json_data['name']
        if 'permission_name' in json_data:
            edit_permission.permission_name = json_data['permission_name']
        
        if 'description' in json_data:
            edit_permission.description = json_data['description']
        db.session.add(edit_permission)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_company_permission():
    try:
        fetch_permission = CompanyRolePermissions.query.all()
        permission = []
        for i in fetch_permission:
                obj = {
                    "id" : i.id,
                    "name": i.name,
                    "permission_name":i.permission_name,
                    "description":i.description
                }
                permission.append(obj)
        return permission
    except:
        return 'Something Went Wrong'

def add_company_roles(json_data):
    try:
        add_roles = CompanyRoles(name = json_data['name'],display_name = json_data['display_name'],description = json_data['description'])
        db.session.add(add_roles)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def edit_company_roles(json_data):
    try:
        edit_roles = CompanyRoles.query.filter_by(id=json_data['id']).first()
        if 'name' in json_data:
            edit_roles.name = json_data['name']
        if 'display_name' in json_data:
            edit_roles.display_name = json_data['display_name']
        if 'description' in json_data:
            edit_roles.description = json_data['description']
        db.session.add(edit_roles)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_company_roles():
    try:
        fetch_roles = CompanyRoles.query.all()
        role = []
        for i in fetch_role:
                obj = {
                    "id" : i.id,
                    "name": i.name,
                    "display_name":i.display_name,
                    "description":i.description
                }
                role.append(obj)
        return role
    except:
        return 'Something Went Wrong'

def add_permission_roles(json_data):
    try:
        add_permission_roles = PermissionRoleConnect(roles_id = json_data['roles_id'],permission_id = json_data['permission_id'])
        db.session.add(add_permission_roles)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def edit_permission_roles(json_data):
    try:
        edit_permission_roles = PermissionRoleConnect.query.filter_by(roles_id=json_data['roles_id']).first()
        if 'roles_id' in json_data:
            edit_permission_roles.roles_id = json_data['roles_id']
        if 'permission_id' in json_data:
            edit_permission_roles.permission_id = json_data['permission_id']
        db.session.add(edit_permission_roles)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def add_users_roles(json_data):
    try:
        add_user_roles = CompanyRoleUser(company_id = json_data['company_id'],roles_id = json_data['roles_id'],user_id = json_data['user_id'])
        db.session.add(add_user_roles)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def edit_users_roles(json_data):
    try:
        edit_users_roles = CompanyRoleUser.query.filter_by(company_id=json_data['company_id'],user_id = json_data['user_id']).first()
        if 'roles_id' in json_data:
            edit_users_roles.roles_id = json_data['roles_id']
        if 'user_id' in json_data:
            edit_users_roles.user_id = json_data['user_id']
        db.session.add(edit_users_roles)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_roles_users(json_data):
    try:
        fetch_roles_users = CompanyRoleUser.query.filter_by(company_id=json_data['company_id'],user_id = json_data['user_id']).first()
        fetch_roles_permission = CompanyRoleUser.query.filter_by().first(id=fetch_roles_users.roles_id).first()
        # roles = []
        roles = {
            "id" : fetch_roles_users.id,
            "company_id": fetch_roles_users.company_id,
            "user_id":fetch_roles_users.user_id,
            "roles_id":fetch_roles_users.roles_id,
            "role":fetch_roles_permission.display_name
        }

        return roles
    except:
        return 'Something Went Wrong'
