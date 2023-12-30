import json
from app import app, db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model1 import *


def delete_recommended_particular_value(json_data,type_id):
    if type_id == 'str':
        recommended_features_value = GlobalProductFeaturesStringRecommended.query.filter_by(id = json_data['id']).first()
        db.session.delete(recommended_features_value)
        db.session.commit()

    if type_id == 'int':
        recommended_features_value = GlobalProductFeaturesIntegerRecommended.query.filter_by(id = json_data['id']).first()
        db.session.delete(recommended_features_value)
        db.session.commit()

    if type_id == 'float':
        recommended_features_value = GlobalProductFeaturesDoubleRecommended.query.filter_by(id = json_data['id']).first()
        db.session.delete(recommended_features_value)
        db.session.commit()

    return 'done'

def remove_recommended_features_values(feature_id,type_id):
    
    if type_id == 'str':
        recommended_features_values = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    if type_id == 'int':
        recommended_features_values = GlobalProductFeaturesIntegerRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    if type_id == 'float':
        recommended_features_values = GlobalProductFeaturesDoubleRecommended.query.filter_by(feature_id = feature_id)
        for value in recommended_features_values:
            db.session.delete(value)
            db.session.commit()

    return "Done"

def delete_features_groups_global(json_data):
    try:
        features_groups = GlobalProductFeaturesGroups.query.filter_by(id=json_data['id']).first()
        db.session.delete(features_groups)
        db.session.commit()
        return "done"
    except:
        return 'Something Went Wrong'

def delete_category_features_global(current_user, json_data):
    # try:
        # if check_current_user_category_id_global(current_user, json_data['id']):
            category_feature_search = GlobalProductCategoryFeature.query.filter_by(id=json_data['id']).first()
            if not category_feature_search:
                return "category_feature_not_found"
            db.session.delete(category_feature_search)
            db.session.commit()
            return 'Feature Delete'
        # else:
        #     return "user_check_fail"
    # except:
    #     return 'Something Went Wrong'

def delete_features(feature_id):
    fetch_feature = GlobalProductCategoryFeature.query.filter_by(id=feature_id).first()
    if fetch_feature.recommendation:
        if fetch_feature.features_datatype_id == 'str':
            recommended_features_values = GlobalProductFeaturesStringRecommended.query.filter_by(feature_id = feature_id)
            for value in recommended_features_values:
                db.session.delete(value)
                db.session.commit()

        if fetch_feature.features_datatype_id == 'int':
            recommended_features_values = GlobalProductFeaturesIntegerRecommended.query.filter_by(feature_id = feature_id)
            for value in recommended_features_values:
                db.session.delete(value)
                db.session.commit()

        if fetch_feature.features_datatype_id == 'float':
            recommended_features_values = GlobalProductFeaturesDoubleRecommended.query.filter_by(feature_id = feature_id)
            for value in recommended_features_values:
                db.session.delete(value)
                db.session.commit()

        # features_recommended = GlobalProductFeaturesRecommended.query.filter_by(feature_id = feature_id)
        # db.session.delete(features_recommended)
        # db.session.commit()
    else:
        if fetch_feature.features_datatype_id == 'str':
            features_values = GlobalProductFeaturesString.query.filter_by(feature_id = feature_id)
            for value in features_values:
                db.session.delete(value)
                db.session.commit()

        if fetch_feature.features_datatype_id == 'int':
            features_values = GlobalProductFeaturesInteger.query.filter_by(feature_id = feature_id)
            for value in features_values:
                db.session.delete(value)
                db.session.commit()

        if fetch_feature.features_datatype_id == 'datetime':
            features_values = GlobalProductFeaturesDate.query.filter_by(feature_id = feature_id)
            for value in features_values:
                db.session.delete(value)
                db.session.commit()

        if fetch_feature.features_datatype_id == 'boolean':
            features_values = GlobalProductFeaturesBoolean.query.filter_by(feature_id = feature_id)
            for value in features_values:
                db.session.delete(value)
                db.session.commit()

        if fetch_feature.features_datatype_id == 'float':
            features_values = GlobalProductFeaturesDouble.query.filter_by(feature_id = feature_id)
            for value in features_values:
                db.session.delete(value)
                db.session.commit()

    features_values = GlobalProductVarientFeatures.query.filter_by(feature_id = feature_id)
    for value in features_values:
        db.session.delete(value)
        db.session.commit()

    db.session.delete(fetch_feature)
    db.session.commit()
    return "Done"
