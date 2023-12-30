import json
from app import app, db
from app.v1.items.model import *

def add_product(json_data):
    try:
        customer_model = CustomersCustomer(name=json_data['name'], active=json_data['active'],description_of_products=json_data['description_of_products'],company_id=json_data['company_id']) 
        db.session.add(customer_model)
        db.session.commit()
        return "done"

    except:
        return 'Something Went Wrong'

def fetch_product(json_data):
    try:
        fetch_products = ItemsProduct.query.filter_by(company_id=json_data['company_id'])
        product = []
        for product in fetch_products:
            obj = {
                "id": fetch_products.id,
                "name": fetch_products.name,
                "company_id":fetch_products.company_id,
                "active":fetch_products.active,
                "description_of_products":fetch_products.description_of_products  
            }
            product.append(obj)
        return product
    except:
        return 'Something Went Wrong'

def edit_product(json_data):
    try:
        edit_products = ItemsProduct.query.filter_by(id=json_data['id']).first()
        if 'name' in json_data:
            edit_products.name = json_data['name']
        if 'company_id' in json_data:
            edit_products.company_id = json_data['company_id']
        
        if 'active' in json_data:
            edit_products.active = json_data['active']
        
        if 'description_of_products' in json_data:
            edit_products.description_of_products = json_data['description_of_products']
        db.session.add(edit_products)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def delete_product(json_data):
    try:
        for i in json_data:
            fetch_products = ItemsProduct.query.filter_by(id=i['id']).first()
            db.session.delete(fetch_products)
            db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'