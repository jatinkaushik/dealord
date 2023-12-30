from app import db
from app.v1.user.model import *

class GlobalProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    parent = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    # sub_category_rel = db.relationship('Sub_Category', backref='category')
    category_features_rel = db.relationship('GlobalProductCategoryFeature', backref='global_product_category')
    products_rel = db.relationship('GlobalProductProductsVarient', backref='global_product_category')
    features_groups_global_rel = db.relationship('GlobalProductFeaturesGroups', backref='global_product_category')