from app import db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model1 import *
from app.v1.general_data.countries.model import *
from app.v1.general_data.datatypes.model import *

class GlobalProductFeaturesGroups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sub_category_id = db.Column(db.Integer, db.ForeignKey('global_product_category.id'))
    order = db.Column(db.Integer)
    category_features_rel = db.relationship('GlobalProductCategoryFeature', backref='global_product_features_groups')    

class GlobalProductCategoryFeature(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    category_id = db.Column(db.Integer, db.ForeignKey('global_product_category.id'))
    features_datatype_id = db.Column(db.String(10), db.ForeignKey('general_data_datatype.abbreviation'))
    unit_types_id = db.Column(db.Integer, db.ForeignKey('general_data_units_types.id'), nullable = True)
    recommendation = db.Column(db.Boolean)
    feature_required = db.Column(db.Boolean, default=False)
    filterable = db.Column(db.Boolean, default=False)
    features_groups_id = db.Column(db.Integer, db.ForeignKey('global_product_features_groups.id'))
    string_features_rel = db.relationship('GlobalProductFeaturesString', backref='global_product_category_feature')
    integer_features_rel = db.relationship('GlobalProductFeaturesInteger', backref='global_product_category_feature')
    double_features_rel = db.relationship('GlobalProductFeaturesDouble', backref='global_product_category_feature')
    datetime_features_rel = db.relationship('GlobalProductFeaturesDate', backref='global_product_category_feature')
    boolean_features_rel = db.relationship('GlobalProductFeaturesBoolean', backref='global_product_category_feature')
    string_features_recommended_rel = db.relationship('GlobalProductFeaturesStringRecommended', backref='global_product_category_feature')
    interger_features_recommended_rel = db.relationship('GlobalProductFeaturesIntegerRecommended', backref='global_product_category_feature')
    double_features_recommended_rel = db.relationship('GlobalProductFeaturesDoubleRecommended', backref='global_product_category_feature')
    recommended_features_global_rel = db.relationship('GlobalProductFeaturesRecommended', backref='global_product_category_feature')
    varient_rel = db.relationship('GlobalProductVarientFeatures', backref='global_product_category_feature')