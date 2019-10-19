from main import db
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.sqlite import BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, VARCHAR
from datetime import datetime
from main import ma


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(255), unique=True)
    user_name = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(255), primary_key=True)
    wallet_add = db.Column(db.String(255))
    type_s = db.Column(db.String(255))

    def __init__(self, user_id, user_name, phone, wallet_add, type_s):
        self.user_id = user_id
        self.user_name = user_name
        self.phone = phone
        self.wallet_add = wallet_add
        self.type_s = type_s

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user_id', 'user_name', 'phone', 'wallet_add', 'type_s')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(255), unique=True)
    user_name = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(255), primary_key=True)
    pin = db.Column(db.Integer)
    photo = db.Column(db.String(255))

    def __init__(self, user_id, user_name, name, phone, is_otp_verified, address_id, email, is_email_verified, password, pin, photo):
        self.user_id = user_id
        self.user_name = user_name
        self.name = name
        self.phone = phone
        self.is_otp_verified = is_otp_verified
        self.address_id = address_id
        self.email = email
        self.is_email_verified = is_email_verified
        self.password = password
        self.pin = pin
        self.photo = photo


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user_id', 'user_name', 'name', 'phone', 'is_otp_verified', 'address_id', 'email', 'is_email_verified', 'password', 'pin', 'photo')

user_schema = UserSchema()
users_schema = UserSchema(many=True)