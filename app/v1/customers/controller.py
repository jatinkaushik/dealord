import json
from app import app, db
from app.v1.customers.model import *

def create_customer(json_data):
    try:
        customer_model = CustomersCustomer(name=json_data['name'], company_id=json_data['company_id']) 
        db.session.add(customer_model)
        db.session.commit()
        if 'customer_info' in json_data:
            info = customer_info(json_data['customer_info'],customer_model.id)
        if 'customer_address' in json_data:
            address = customer_address(json_data['customer_address'],customer_model.id)
        return "done"

    except:
        return 'Something Went Wrong'

def fetch_customer(customer_id): 
    
    try:
        fetch_customer = CustomersCustomer.query.filter_by(id=customer_id).first()
        obj = {
                "id": fetch_customer.id,
                "name": fetch_customer.name,
                "company_id":fetch_customer.company_id
                
            }
        return obj
    except:
        return 'Something Went Wrong'

def customer_info(json_data,customer_id):
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
        customer_info_obj = CustomersInfo(
            customer_id= customer_id,
            legal_name = legal_name,
            gstin_no = gstin_no,
            cin_no = cin_no,
            website = website,
            email = email,
            phone_no = phone_no,
            fax = fax) 
        db.session.add(customer_info_obj)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_customer_info(customer_id):
    try:
        fetch_customer_info = CustomersInfo.query.filter_by(customer_id=customer_id).first()
        obj = {
                "id": fetch_customer_info.id,
                "customer_id":fetch_customer_info.customer_id,
                "legal_name":fetch_customer_info.legal_name,
                "gstin_no":fetch_customer_info.gstin_no,
                "cin_no":fetch_customer_info.cin_no,
                "website":fetch_customer_info.website,
                "email":fetch_customer_info.email,
                "phone_no":fetch_customer_info.phone_no,
                "fax":fetch_customer_info.fax
                
            }
        return obj
    except:
        return 'Something Went Wrong'

def customer_address(json_data,customer_id):
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
        customer_address_obj = CustomersAddress(
            customer_id= customer_id,
            address_line = address_line,
            district = district,
            city_town = city_town,
            landmark = landmark,
            state = state,
            country = country,
            pin_code = pin_code)
        db.session.add(customer_address_obj)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_customer_address(customer_id):
    try:
        fetch_customer_address = CustomersAddress.query.filter_by(customer_id=customer_id).first()
        obj = {
                "id": fetch_customer_address.id,
                "customer_id":fetch_customer_address.customer_id,
                "address_line_1":fetch_customer_address.address_line,
                "district":fetch_customer_address.district,
                "city_town":fetch_customer_address.city_town,
                "landmark":fetch_customer_address.landmark,
                "state":fetch_customer_address.state,
                "country":fetch_customer_address.country,
                "pin_code":fetch_customer_address.pin_code
                
            }
        return obj
    except:
        return 'Something Went Wrong'