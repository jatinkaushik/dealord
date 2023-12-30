import json
from app import app, db
from app.v1.vendors.model import *

def create_vendor(json_data):
    try:
        vendor_model = VendorsVendor(name=json_data['name'], company_id=json_data['company_id']) 
        db.session.add(vendor_model)
        db.session.commit()
        return "done"

    except:
        return 'Something Went Wrong'

def fetch_vendor(vendor_id):
    try:
        fetch_vendor = VendorsVendor.query.filter_by(id=vendor_id).first()
        obj = {
                "id": fetch_vendor.id,
                "name": fetch_vendor.name,
                "company_id":fetch_vendor.company_id
                
            }
        return obj
    except:
        return 'Something Went Wrong'


def vendor_info(json_data):
    try:
        vendor_info_obj = VendorsInfo(vendor_id= json_data['vendor_id'],legal_name = json_data['legal_name'],gstin_no = json_data['gstin_no'],cin_no = json_data['cin_no'],website = json_data['website'],email = json_data['email'],phone_no = json_data['phone_no'],fax = json_data['fax']) 
        db.session.add(vendor_model)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_vendor_info(vendor_id):
    try:
        fetch_vendor_info = VendorsInfo.query.filter_by(vendor_id=vendor_id).first()
        obj = {
                "id": fetch_vendor_info.id,
                "vendor_id":fetch_vendor_info.vendor_id,
                "legal_name":fetch_vendor_info.legal_name,
                "gstin_no":fetch_vendor_info.gstin_no,
                "cin_no":fetch_vendor_info.cin_no,
                "website":fetch_vendor_info.website,
                "email":fetch_vendor_info.email,
                "phone_no":fetch_vendor_info.phone_no,
                "fax":fetch_vendor_info.fax
                
            }
        return obj
    except:
        return 'Something Went Wrong'

def vendor_address(json_data):
    try:
        vendor_address_obj = VendorsAddress(vendor_id= json_data['vendor_id'],address_line_1 = json_data['address_line_1'],address_line_2 = json_data['address_line_2'],district = json_data['district'],city_town = json_data['city_town'],landmark = json_data['landmark'],state = json_data['state'],country = json_data['country'])
        db.session.add(vendor_address)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def fetch_vendor_address(vendor_id):
    try:
        fetch_vendor_address = VendorsAddress.query.filter_by(vendor_id=vendor_id).first()
        obj = {
                "id": fetch_vendor_address.id,
                "vendor_id":fetch_vendor_address.vendor_id,
                "address_line_1":fetch_vendor_address.address_line_1,
                "address_line_2":fetch_vendor_address.address_line_2,
                "district":fetch_vendor_address.district,
                "city_town":fetch_vendor_address.city_town,
                "landmark":fetch_vendor_address.landmark,
                "state":fetch_vendor_address.state,
                "country":fetch_vendor_address.country,
                "pin_code":fetch_vendor_address.pin_code
                
            }
        return obj
    except:
        return 'Something Went Wrong'