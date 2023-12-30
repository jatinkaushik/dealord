import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model1 import *
from app.v1.global_product.controller.features.add import *
from app.v1.global_product.controller.features.delete import *

def edit_category_features_global(json_data):
    # try:
        category_feature_search = GlobalProductCategoryFeature.query.filter_by(id=json_data['id']).first()
        if not category_feature_search:
            return "category_feature_not_found"
        if 'name' in json_data:
            category_feature_search.name = json_data['name']

        if 'type' in json_data:
            category_feature_search.features_datatype_id = json_data['type']


        if 'category_id' in json_data:
            category_feature_search.category_id = json_data['category_id']
        
        if 'unit' in json_data:
            category_feature_search.unit_types_id = json_data['unit']

        if 'groups_id' in json_data:
            category_feature_search.features_groups_id = json_data['groups_id']
        
        if 'filterable' in json_data:
            category_feature_search.filterable = json_data['filterable']
        
        if 'is_required' in json_data:
            category_feature_search.feature_required = json_data['is_required']

        if 'is_recommendation' in json_data:
            category_feature_search.recommendation = json_data['is_recommendation']
            # if category_feature_search.recommendation == True:
                
            if category_feature_search.recommendation == False:
                # delete_recommended_features1 = delete_recommended_features(category_feature_search.id)
                delete_recommended_features_values1 = remove_recommended_features_values(category_feature_search.id,category_feature_search.features_datatype_id)

        db.session.add(category_feature_search)
        db.session.commit()
        return 'Category Features Edited'

    # except:
    #     return 'Something Went Wrong'



def edit_category_features_with_check_global(json_data):
    # try:
        category_feature_search = GlobalProductCategoryFeature.query.filter_by(id=json_data['id']).first()
        if not category_feature_search:
            return "category_feature_not_found"
        
        if 'name' in json_data:
            if json_data['name'] != category_feature_search.name:
                category_feature_search.name = json_data['name']

        if 'type' in json_data:
            if json_data['type'] != category_feature_search.features_datatype_id:
                delete_recommended_features_values1 = remove_recommended_features_values(category_feature_search.id,category_feature_search.features_datatype_id)
                category_feature_search.features_datatype_id = json_data['type']



        # if 'category_id' in json_data:
        #     if json_data['category_id'] != category_feature_search.category_id:
        #         category_feature_search.category_id = json_data['category_id']
        
        if 'unit' in json_data:
            if json_data['unit'] != category_feature_search.unit_types_id:
                if category_feature_search.unit_types_id == False:
                    category_feature_search.unit_types_id = json_data['unit']
                else:
                    category_feature_search.unit_types_id = json_data['unit']

        if 'groups_id' in json_data:
            if json_data['groups_id'] != category_feature_search.features_groups_id:
                category_feature_search.features_groups_id = json_data['groups_id']
        
        if 'filterable' in json_data:
            if json_data['filterable'] != category_feature_search.filterable:
                category_feature_search.filterable = json_data['filterable']
        
        if 'is_required' in json_data:
            if json_data['is_required'] != category_feature_search.feature_required:
                category_feature_search.feature_required = json_data['is_required']

        if 'is_recommendation' in json_data:
            recommendation_options = json_data['recommendation_options']
            if json_data['is_recommendation'] != category_feature_search.recommendation:
                category_feature_search.recommendation = json_data['is_recommendation']
                if category_feature_search.recommendation == True:
                    # for add in recommendation_options['add']:
                    add_recommendation = recommendation_data(recommendation_options['add'],category_feature_search.id,category_feature_search.features_datatype_id)   

                if category_feature_search.recommendation == False:
                    # delete_recommended_features1 = delete_recommended_features(category_feature_search.id)
                    delete_recommended_features_values1 = remove_recommended_features_values(category_feature_search.id,category_feature_search.features_datatype_id)
            else:
                if category_feature_search.recommendation == True:
                    if recommendation_options['edit']:
                        for edit in recommendation_options['edit']:
                            edit_recommendation = edit_recommended_particular_value(edit,category_feature_search.features_datatype_id)

                    if recommendation_options['delete']:
                        for delete in recommendation_options['delete']:
                            delete_recommendation = delete_recommended_particular_value(delete,category_feature_search.features_datatype_id)

                    if recommendation_options['add']:
                        # for add in recommendation_options['add']:
                        add_recommendation = recommendation_data(recommendation_options['add'],category_feature_search.id,category_feature_search.features_datatype_id)

        db.session.add(category_feature_search)
        db.session.commit()
        # features = fetch_features_global(category_feature_search.id)
        return "features"

    # except:
    #     return 'Something Went Wrong'

def edit_recommended_particular_value(json_data,type_id):
    if type_id == 'str':
        recommendation_search = GlobalProductFeaturesStringRecommended.query.filter_by(id=json_data['id']).first()
        if 'feature_id' in json_data:
            recommendation_search.feature_id = json_data['feature_id']

        if 'value' in json_data:
            recommendation_search.feature_value = json_data['value']
    if type_id == 'int':
        recommendation_search = GlobalProductFeaturesIntegerRecommended.query.filter_by(id=json_data['id']).first()
        if 'feature_id' in json_data:
            recommendation_search.feature_id = json_data['feature_id']

        if 'value' in json_data:
            recommendation_search.feature_value = json_data['value']
    if type_id == 'float':
        recommendation_search = GlobalProductFeaturesDoubleRecommended.query.filter_by(id=json_data['id']).first()
        if 'feature_id' in json_data:
            recommendation_search.feature_id = json_data['feature_id']

        if 'value' in json_data:
            recommendation_search.feature_value = json_data['value']

    db.session.add(recommendation_search)
    db.session.commit()
    return 'done'

