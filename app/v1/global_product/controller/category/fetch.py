import json
from app import app, db
from app.v1.global_product.model.category.category import *

#----------------------- Fetch Category ------------------

def fetch_category_global():
    # data = current_user.category_global_rel
    data = GlobalProductCategory.query.filter_by(parent=None)
    output = []
    for i in data:
        obj = {
            "id": i.id,
            "name": i.name,
            "child": fetch_sub_category(i.id)
        }
        output.append(obj)
    
    return output
    # check_category = Category.query.filter_by(name=json_data['name']).first()  

    # if check_category:
    #     return "Done"

#--------------Fetch Sub category With parent id---------------

def fetch_sub_category(cat_id):
    parent_check = GlobalProductCategory.query.filter_by(parent=cat_id)
    if not parent_check:
        return "category_not_found"
    sub_category = []
    for i in parent_check:
        obj = {
            "id" : i.id,
            "name": i.name,
            "user_id": i.user_id,
            "parent_id": i.parent,
            "child": fetch_sub_category(i.id)
        }
        sub_category.append(obj)
        
    return sub_category