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
        customer_info_obj = CustomersInfo(customer_id= json_data['customer_id'],
        legal_name = json_data['legal_name'],gstin_no = json_data['gstin_no'],cin_no = json_data['cin_no'],website = json_data['website'],email = json_data['email'],phone_no = json_data['phone_no'],fax = json_data['fax']) 
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
    try:
        customer_address_obj = CustomersAddress(customer_id= customer_id,address_line_1 = json_data['address_line_1'],address_line_2 = json_data['address_line_2'],district = json_data['district'],city_town = json_data['city_town'],landmark = json_data['landmark'],state = json_data['state'],country = json_data['country'])
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
                "address_line_1":fetch_customer_address.address_line_1,
                "address_line_2":fetch_customer_address.address_line_2,
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