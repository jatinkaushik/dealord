from app import db
from app.v1.user.model import *

class Category_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    parent = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # sub_category_rel = db.relationship('Sub_Category', backref='category')
    category_features_rel = db.relationship('Category_Feature_Global', backref='category__global')
    products_rel = db.relationship('Products_Global', backref='category__global')
    features_groups_global_rel = db.relationship('Features_Groups_Global', backref='category__global')

# class Sub_Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40))
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     sub_category_features_rel = db.relationship('Sub_Category_Feature', backref='sub__category')
#     products_rel = db.relationship('Products', backref='sub__category')

class Features_Datatype_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category_features_rel = db.relationship('Category_Feature_Global', backref='features__datatype__global')


class Features_Groups_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    sub_category_id = db.Column(db.Integer, db.ForeignKey('category__global.id'))
    category_features_rel = db.relationship('Category_Feature_Global', backref='features__groups__global')    

class Category_Feature_Global(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    category_id = db.Column(db.Integer, db.ForeignKey('category__global.id'))
    features_datatype_id = db.Column(db.Integer, db.ForeignKey('features__datatype__global.id'))
    unit = db.Column(db.Integer, nullable=True)
    recommendation = db.Column(db.Boolean)
    features_groups_id = db.Column(db.Integer, db.ForeignKey('features__groups__global.id'))
    string_features_rel = db.relationship('String_Features_Global', backref='category__feature__global')
    integer_features_rel = db.relationship('Integer_Features_Global', backref='category__feature__global')
    double_features_rel = db.relationship('Double_Features_Global', backref='category__feature__global')
    datetime_features_rel = db.relationship('Date_Features_Global', backref='category__feature__global')
    boolean_features_rel = db.relationship('Boolean_Features_Global', backref='category__feature__global')
    string_features_recommended_rel = db.relationship('String_Features_Recommended_Global', backref='category__feature__global')
    interger_features_recommended_rel = db.relationship('Integer_Features_Recommended_Global', backref='category__feature__global')
    double_features_recommended_rel = db.relationship('Double_Features_Recommended_Global', backref='category__feature__global')
    recommended_features_global_rel = db.relationship('Recommended_Features_Global', backref='category__feature__global')
    varient_rel = db.relationship('Varient_Global', backref='category__feature__global')


class Products_Global(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category__global.id'))
    string_features_rel = db.relationship('String_Features_Global', backref='products__global')
    integer_features_rel = db.relationship('Integer_Features_Global', backref='products__global')
    double_features_rel = db.relationship('Double_Features_Global', backref='products__global')
    datetime_features_rel = db.relationship('Date_Features_Global', backref='products__global')
    boolean_features_rel = db.relationship('Boolean_Features_Global', backref='products__global')
    Extra_features_rel = db.relationship('Extra_Features_Global', backref='products__global')
    varient_rel = db.relationship('Varient_Global', backref='products__global')


class String_Features_Global(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.String(1000))
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))
    
class Integer_Features_Global(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.Integer)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))

class Double_Features_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Float)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))


class Date_Features_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.DateTime)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))

class Boolean_Features_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Boolean)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))

class Extra_Features_Global(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(40))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))
    feature_type_id = db.Column(db.Integer)
    units = db.Column(db.Integer)

class Varient_Global(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    category_feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))

class String_Features_Recommended_Global(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.String(1000))
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    boolean_features_rel = db.relationship('Recommended_Features_Global', backref='string__features__recommended__global')

class Integer_Features_Recommended_Global(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    feature_value = db.Column(db.Integer)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    boolean_features_rel = db.relationship('Recommended_Features_Global', backref='integer__features__recommended__global')

class Double_Features_Recommended_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feature_value = db.Column(db.Float)
    feature_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    boolean_features_rel = db.relationship('Recommended_Features_Global', backref='double__features__recommended__global')

class Recommended_Features_Global(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_feature_global_id = db.Column(db.Integer, db.ForeignKey('category__feature__global.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products__global.id'))
    string_seleted_id = db.Column(db.Integer, db.ForeignKey('string__features__recommended__global.id'))
    integer_seleted_id = db.Column(db.Integer, db.ForeignKey('integer__features__recommended__global.id'))
    double_seleted_id = db.Column(db.Integer, db.ForeignKey('double__features__recommended__global.id'))