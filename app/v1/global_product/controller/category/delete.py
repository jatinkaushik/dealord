import json
from app import app, db
from app.v1.global_product.model.category.category import *

#-------------------- Delete Category-------------------

def delete_category_global(current_user, json_data):
    try:
        # if check_current_user_category_id_global(current_user, json_data['id']):
        category_search = GlobalProductCategory.query.filter_by(id=json_data['id']).first()
        if not category_search:
            return "category_not_found"
        db.session.delete(category_search)
        db.session.commit()
        # return fetch_category_global()
        return "done"
        # else:
        #     return "user_check_fail"    
    except:
        return 'Something Went Wrong'