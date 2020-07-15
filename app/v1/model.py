from app import db

class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    iso3 = db.Column(db.String(5))
    iso2 = db.Column(db.String(5))
    phonecode = db.Column(db.String(200))
    capital = db.Column(db.String(200))
    currency = db.Column(db.String(200))
    native = db.Column(db.String(200))
    emoji = db.Column(db.String(200))
    emojiU = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    flag = db.Column(db.Boolean)
    wikiDataId = db.Column(db.String(200))
    states_rel = db.relationship('States', backref='countries')

class States(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country_id = db.Column(db.Integer,db.ForeignKey('countries.id'))
    country_code = db.Column(db.String(5))
    fips_code = db.Column(db.String(200))
    iso2 = db.Column(db.String(5))
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    flag = db.Column(db.Boolean)
    wikiDataId = db.Column(db.String(200))  
    states_rel = db.relationship('States', backref='countries') 

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    state_id = db.Column(db.Integer,db.ForeignKey('states.id'))
    state_code = db.Column(db.String(5))
    country_id = db.Column(db.Integer,db.ForeignKey('countries.id'))
    country_code = db.Column(db.String(5))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    flag = db.Column(db.Boolean)
    wikiDataId = db.Column(db.String(200))
