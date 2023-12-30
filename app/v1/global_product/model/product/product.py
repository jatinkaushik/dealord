from app import db
from app.v1.global_product.model.category.category import *
from app.v1.global_product.model.product.product import *

class GlobalProductProducts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    varient = db.Column(db.Boolean)
    products_varient_rel = db.relationship('GlobalProductProductsVarient', backref='global_product_products')
    varient_rel = db.relationship('GlobalProductVarientFeatures', backref='global_product_products')


class GlobalProductProductsVarient(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))
    name = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('global_product_category.id'))
    country_of_origin = db.Column(db.Integer, db.ForeignKey('countries.id'))
    description_of_products = db.Column(db.String(2000)) 
    is_product_features_added = db.Column(db.Boolean, default=False)
    product_live = db.Column(db.Boolean, default=False)
    product_approve = db.Column(db.Boolean, default=False)
    master_product = db.Column(db.Integer)
    string_features_rel = db.relationship('GlobalProductFeaturesString', backref='global_product_products_varient')
    integer_features_rel = db.relationship('GlobalProductFeaturesInteger', backref='global_product_products_varient')
    double_features_rel = db.relationship('GlobalProductFeaturesDouble', backref='global_product_products_varient')
    datetime_features_rel = db.relationship('GlobalProductFeaturesDate', backref='global_product_products_varient')
    boolean_features_rel = db.relationship('GlobalProductFeaturesBoolean', backref='global_product_products_varient')
    Extra_features_rel = db.relationship('GlobalProductFeaturesExtra', backref='global_product_products_varient')
    recommended_features_global_rel = db.relationship('GlobalProductFeaturesRecommended', backref='global_product_products_varient')
    products_image_rel = db.relationship('GlobalProductProductsImage', backref='global_product_products_varient')
    varient_rel = db.relationship('GlobalProductVarientFeatures', backref='global_product_products_varient')

class GlobalProductVarientFeatures(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))
    product_varient_id = db.Column(db.Integer, db.ForeignKey('global_product_products_varient.id'))