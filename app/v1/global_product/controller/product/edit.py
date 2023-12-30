import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model.product.product import *
from app.v1.global_product.model1 import *

def edit_product_varient(image,json_data):
    try:
        product = json.loads(json_data['json'])
        product_varient_search = GlobalProductProductsVarient.query.filter_by(id=product['id']).first()
        
        if 'name' in product:
            if product['name'] != product_varient_search.name:
                product_varient_search.name = product['name']

        if 'product_id' in product:
            if product['product_id'] != product_varient_search.product_id:
                product_varient_search.product_id = product['product_id'] 

        if 'category_id' in product:
            if product['category_id'] != product_varient_search.category_id:
                product_varient_search.category_id = product['category_id']
        
        if 'country_of_origin' in product:
            if product['country_of_origin'] != product_varient_search.country_of_origin:
                product_varient_search.country_of_origin = product['country_of_origin']

        if 'description_of_products' in product:
            if product['description_of_products'] != product_varient_search.description_of_products:
                product_varient_search.description_of_products = product['description_of_products']

        if 'is_product_features_added' in product:
            if product['is_product_features_added'] != product_varient_search.is_product_features_added:
                product_varient_search.is_product_features_added = product['is_product_features_added']

        if 'product_live' in product:
            if product['product_live'] != product_varient_search.product_live:
                product_varient_search.product_live = product['product_live']

        if 'product_approve' in product:
            if product['product_approve'] != product_varient_search.product_approve:
                product_varient_search.product_approve = product['product_approve']
        
        if 'master_product' in product:
            if product['master_product'] != product_varient_search.master_product:
                product_varient_search.master_product = product['master_product']

        
    except:
        return 'Something Went Wrong'
