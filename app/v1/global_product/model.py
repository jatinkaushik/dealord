from app import db
from app.v1.user.model import *

class GlobalProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    parent = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_user.id'))
    # sub_category_rel = db.relationship('Sub_Category', backref='category')
    category_features_rel = db.relationship('GlobalProductCategoryFeature', backref='global_product_category')
    products_rel = db.relationship('GlobalProductProducts', backref='global_product_category')
    features_groups_global_rel = db.relationship('GlobalProductFeaturesGroups', backref='global_product_category')

# class Sub_Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     sub_category_features_rel = db.relationship('Sub_Category_Feature', backref='sub__category')
#     products_rel = db.relationship('Products', backref='sub__category')

class GlobalProductFeaturesDatatype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category_features_rel = db.relationship('GlobalProductCategoryFeature', backref='global_product_features_datatype')


class GlobalProductFeaturesGroups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sub_category_id = db.Column(db.Integer, db.ForeignKey('global_product_category.id'))
    category_features_rel = db.relationship('GlobalProductCategoryFeature', backref='global_product_features_groups')    

class GlobalProductCategoryFeature(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    category_id = db.Column(db.Integer, db.ForeignKey('global_product_category.id'))
    features_datatype_id = db.Column(db.Integer, db.ForeignKey('global_product_features_datatype.id'))
    unit_id = db.Column(db.Integer, db.ForeignKey('global_product_features_units_types.id'))
    recommendation = db.Column(db.Boolean)
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
    varient_rel = db.relationship('GlobalProductVarient', backref='global_product_category_feature')


class GlobalProductProducts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('global_product_category.id'))
    string_features_rel = db.relationship('GlobalProductFeaturesString', backref='global_product_products')
    integer_features_rel = db.relationship('GlobalProductFeaturesInteger', backref='global_product_products')
    double_features_rel = db.relationship('GlobalProductFeaturesDouble', backref='global_product_products')
    datetime_features_rel = db.relationship('GlobalProductFeaturesDate', backref='global_product_products')
    boolean_features_rel = db.relationship('GlobalProductFeaturesBoolean', backref='global_product_products')
    Extra_features_rel = db.relationship('GlobalProductFeaturesExtra', backref='global_product_products')
    recommended_features_global_rel = db.relationship('GlobalProductFeaturesRecommended', backref='global_product_products')
    varient_rel = db.relationship('GlobalProductVarient', backref='global_product_products')


class GlobalProductFeaturesString(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.String(1000))
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))
    
class GlobalProductFeaturesInteger(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.Integer)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))

class GlobalProductFeaturesDouble(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Float)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))


class GlobalProductFeaturesDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.DateTime)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))

class GlobalProductFeaturesBoolean(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Boolean)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))

class GlobalProductFeaturesExtra(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))
    feature_type_id = db.Column(db.Integer)
    units = db.Column(db.Integer)

class GlobalProductVarient(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category_feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))

class GlobalProductFeaturesStringRecommended(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.String(1000))
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    boolean_features_rel = db.relationship('GlobalProductFeaturesRecommended', backref='global_product_features_string_recommended')

class GlobalProductFeaturesIntegerRecommended(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.Integer)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    boolean_features_rel = db.relationship('GlobalProductFeaturesRecommended', backref='global_product_features_integer_recommended')

class GlobalProductFeaturesDoubleRecommended(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Float)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    boolean_features_rel = db.relationship('GlobalProductFeaturesRecommended', backref='global_product_features_double_recommended')

class GlobalProductFeaturesRecommended(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_product_products.id'))
    string_seleted_id = db.Column(db.Integer, db.ForeignKey('global_product_features_string_recommended.id'))
    integer_seleted_id = db.Column(db.Integer, db.ForeignKey('global_product_features_integer_recommended.id'))
    double_seleted_id = db.Column(db.Integer, db.ForeignKey('global_product_features_double_recommended.id'))

class GlobalProductFeaturesUnitsTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # features_id = db.Column(db.Integer, db.ForeignKey('global_product_category_feature.id'))
    category_features_rel = db.relationship('GlobalProductCategoryFeature', backref= 'global_product_features_units_types')
    units_rel = db.relationship('GlobalProductFeaturesUnits', backref='global_product_features_units_types')

class GlobalProductFeaturesUnits(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    units_type_id = db.Column(db.Integer, db.ForeignKey('global_product_features_units_types.id'))
    order = db.Column(db.Integer)
