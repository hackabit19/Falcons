from main import db
from flask_marshmallow import Marshmallow
from sqlalchemy.dialects.sqlite import BLOB, BOOLEAN, CHAR, DATE, DATETIME, DECIMAL, FLOAT, INTEGER, NUMERIC, SMALLINT, TEXT, TIME, TIMESTAMP, VARCHAR
from datetime import datetime
from main import ma


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.String(255), unique=True)
    user_name = db.Column(db.String(255))
    phone = db.Column(db.String(255), primary_key=True)
    wallet_add = db.Column(db.String(255))
    password = db.Column(db.String(255))
    type_s = db.Column(db.String(255))

    def __init__(self, user_id, user_name, phone, wallet_add, password, type_s):
        self.user_id = user_id
        self.user_name = user_name
        self.phone = phone
        self.wallet_add = wallet_add
        self.password = password
        self.type_s = type_s

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('user_id', 'user_name', 'phone', 'wallet_add', 'password', 'type_s')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Slave(db.Model):
    __tablename__ = 'slaves'
    slave_id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.String(255))
    data_amount = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, time_stamp, data_amount, phone):
        self.time_stamp = time_stamp
        self.data_amount = data_amount
        self.phone = phone

class SlaveSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('slave_id', 'time_stamp', 'data_amount', 'phone')

slave_schema = SlaveSchema()
slaves_schema = SlaveSchema(many=True)

class ClientTrans(db.Model):
    __tablename__ = 'clienttrans'
    clienttrans_id = db.Column(db.Integer, primary_key=True)
    time_stamp_start = db.Column(db.String(255))
    time_stamp_end = db.Column(db.String(255))
    data_amount = db.Column(db.String(255))
    status = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, time_stamp_start, time_stamp_end, data_amount, status, phone):
        self.time_stamp_start = time_stamp_start
        self.time_stamp_end = time_stamp_end
        self.data_amount = data_amount
        self.status = status
        self.phone = phone

class ClientTransSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('clienttrans_id', 'time_stamp_start', 'time_stamp_end', 'data_amount', 'status', 'phone')

clienttrans_schema = ClientTransSchema()
clienttranss_schema = ClientTransSchema(many=True)

class SlaveTrans(db.Model):
    __tablename__ = 'slavetrans'
    slavetrans_id = db.Column(db.Integer, primary_key=True)
    time_stamp_start = db.Column(db.String(255))
    time_stamp_end = db.Column(db.String(255))
    data_amount = db.Column(db.String(255))
    status = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, time_stamp_start, time_stamp_end, data_amount, status, phone):
        self.time_stamp_start = time_stamp_start
        self.time_stamp_end = time_stamp_end
        self.data_amount = data_amount
        self.status = status
        self.phone = phone

class SlaveTransSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('slavetrans_id', 'time_stamp_start', 'time_stamp_end', 'data_amount', 'status', 'phone')

slavetrans_schema = SlaveTransSchema()
slavetranss_schema = SlaveTransSchema(many=True)
