from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(1000))
    token_s = db.relationship('Token', backref='user')

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    # def is_valid(self):
    #     return self.is_active




class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tokens = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class RegistrationForm(Form):
#     username = TextField('Username', [validators.Length(min=4, max=20)])
#     email = TextField('Email Address', [validators.Length(min=6, max=50)])
#     password = PasswordField('New Password')
#     phone = TextField('Phone No', [validators.Length(min=4, max=15)])
