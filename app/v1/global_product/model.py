from app import db
from app.v1.user.model import *

class GlobalCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    parent = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # sub_category_rel = db.relationship('Sub_Category', backref='category')
    category_features_rel = db.relationship('GlobalCategoryFeature', backref='global_category')
    products_rel = db.relationship('GlobalProducts', backref='global_category')
    features_groups_global_rel = db.relationship('GlobalFeaturesGroups', backref='global_category')

# class Sub_Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     sub_category_features_rel = db.relationship('Sub_Category_Feature', backref='sub__category')
#     products_rel = db.relationship('Products', backref='sub__category')

class GlobalFeaturesDatatype(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category_features_rel = db.relationship('GlobalCategoryFeature', backref='global_features_datatype')


class GlobalFeaturesGroups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sub_category_id = db.Column(db.Integer, db.ForeignKey('global_category.id'))
    category_features_rel = db.relationship('GlobalCategoryFeature', backref='global_features_groups')    

class GlobalCategoryFeature(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    category_id = db.Column(db.Integer, db.ForeignKey('global_category.id'))
    features_datatype_id = db.Column(db.Integer, db.ForeignKey('global_features_datatype.id'))
    unit = db.Column(db.Integer, nullable=True)
    recommendation = db.Column(db.Boolean)
    features_groups_id = db.Column(db.Integer, db.ForeignKey('global_features_groups.id'))
    string_features_rel = db.relationship('GlobalFeaturesString', backref='global_category_feature')
    integer_features_rel = db.relationship('GlobalFeaturesInteger', backref='global_category_feature')
    double_features_rel = db.relationship('GlobalFeaturesDouble', backref='global_category_feature')
    datetime_features_rel = db.relationship('GlobalFeaturesDate', backref='global_category_feature')
    boolean_features_rel = db.relationship('GlobalFeaturesBoolean', backref='global_category_feature')
    string_features_recommended_rel = db.relationship('GlobalFeaturesStringRecommended', backref='global_category_feature')
    interger_features_recommended_rel = db.relationship('GlobalFeaturesIntegerRecommended', backref='global_category_feature')
    double_features_recommended_rel = db.relationship('GlobalFeaturesDoubleRecommended', backref='global_category_feature')
    recommended_features_global_rel = db.relationship('GlobalFeaturesRecommended', backref='global_category_feature')
    varient_rel = db.relationship('GlobalVarient', backref='global_category_feature')


class GlobalProducts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('global_category.id'))
    string_features_rel = db.relationship('GlobalFeaturesString', backref='global_products')
    integer_features_rel = db.relationship('GlobalFeaturesInteger', backref='global_products')
    double_features_rel = db.relationship('GlobalFeaturesDouble', backref='global_products')
    datetime_features_rel = db.relationship('GlobalFeaturesDate', backref='global_products')
    boolean_features_rel = db.relationship('GlobalFeaturesBoolean', backref='global_products')
    Extra_features_rel = db.relationship('GlobalFeaturesExtra', backref='global_products')
    recommended_features_global_rel = db.relationship('GlobalFeaturesRecommended', backref='global_products')
    varient_rel = db.relationship('GlobalVarient', backref='global_products')


class GlobalFeaturesString(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.String(1000))
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))
    
class GlobalFeaturesInteger(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.Integer)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))

class GlobalFeaturesDouble(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Float)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))


class GlobalFeaturesDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.DateTime)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))

class GlobalFeaturesBoolean(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Boolean)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))

class GlobalFeaturesExtra(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))
    feature_type_id = db.Column(db.Integer)
    units = db.Column(db.Integer)

class GlobalVarient(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category_feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))

class GlobalFeaturesStringRecommended(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.String(1000))
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    boolean_features_rel = db.relationship('GlobalFeaturesRecommended', backref='global_features_string_recommended')

class GlobalFeaturesIntegerRecommended(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.Integer)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    boolean_features_rel = db.relationship('GlobalFeaturesRecommended', backref='global_features_integer_recommended')

class GlobalFeaturesDoubleRecommended(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Float)
    feature_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    boolean_features_rel = db.relationship('GlobalFeaturesRecommended', backref='global_features_double_recommended')

class GlobalFeaturesRecommended(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_feature_global_id = db.Column(db.Integer, db.ForeignKey('global_category_feature.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('global_products.id'))
    string_seleted_id = db.Column(db.Integer, db.ForeignKey('global_features_string_recommended.id'))
    integer_seleted_id = db.Column(db.Integer, db.ForeignKey('global_features_integer_recommended.id'))
    double_seleted_id = db.Column(db.Integer, db.ForeignKey('global_features_double_recommended.id'))