import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.controller.category.fetch import *


# ------------------ create New category ------------------

def create_category_global(current_user, json_data): 
    try:
        category_model = GlobalProductCategory(name=json_data['name'], parent=json_data['parent'], user_id=current_user.id) 
        db.session.add(category_model)
        db.session.commit()
        return fetch_category_global()
        # return "done"

    except:
        return 'Something Went Wrong'