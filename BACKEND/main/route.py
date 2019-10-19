from flask import request, jsonify
from main import app
from main.model import (
    User,
    user_schema,
    users_schema,
    UserSchema,
    Request,
    request_schema,
    requests_schema,
    RequestSchema,
    Data,
    data_schema,
    datas_schema,
    DataSchema,
    SharedData,
    SharedDataSchema,
    shareddata_schema,
    shareddatas_schema,
    Request,
    RequestSchema,
    request_schema,
    requests_schema,
    Notifications,
    NotificationsSchema,
    notifications_schema,
    notificationss_schema,
    Package,
    PackageSchema,
    package_schema,
    packages_schema,
    Booking,
    BookingSchema,
    booking_schema,
    bookings_schema,
    Payment,
    PaymentSchema,
    payment_schema,
    payments_schema,
)
from flask_marshmallow import Marshmallow
from main import db


@app.route("/")
def func():
    return "working"
@app.route("/isRegisteredUser/<phone>", methods=["GET"])
def isRegisteredUser(phone):
    data = User.query.get(phone)
    if (data.phone != phone) :
        return "False"
    else :
        return "True"

@app.route("/isValidUser", methods=["GET"])
def isValidUser():
    phone = request.args['phone'].encode('ascii','ignore')
    password = request.args['password'].encode('ascii','ignore')
    user_name = request.args['user_name'].encode('ascii','ignore')



    data = User.query.get(phone)
    # return user_schema.jsonify(data)

    if(data.password == password and data.user_name == user_name) :
        return "True"
    else :
        return "False"



@app.route("/doRegistration", methods=["POST"])
def doRegistration():

    user_id = request.json['user_id']
    user_name = request.json['user_name'].encode('ascii','ignore')
    name = request.json['name'].encode('ascii','ignore')
    phone = request.json['phone'].encode('ascii','ignore')
    is_otp_verified = request.json['is_otp_verified']
    address_id = request.json['address_id']
    email = request.json['email'].encode('ascii','ignore')
    is_email_verified = request.json['is_email_verified']
    password = request.json['password'].encode('ascii','ignore')
    pin = request.json['pin']
    photo = request.json['photo'].encode('ascii','ignore')

    new_user = User(user_id, user_name, name, phone, is_otp_verified, address_id, email, is_email_verified, password, pin, photo)

    db.session.add(new_user)
    db.session.commit()
    return "True"

@app.route("/getRegistration/<phone>", methods=["GET"])
def reg_detail(phone):
    user = User.query.get(phone)
    return user_schema.jsonify(user)

# endpoint to update user
@app.route("/updateRegistration/<phone>", methods=["PUT"])
def reg_update(phone):
    user = User.query.get(phone)

    user_id = request.json['user_id']
    user_name = request.json['user_name'].encode('ascii','ignore')
    name = request.json['name'].encode('ascii','ignore')
    phone = request.json['phone'].encode('ascii','ignore')
    is_otp_verified = int(request.json['is_otp_verified'])
    address_id = request.json['address_id']
    email = request.json['email'].encode('ascii','ignore')
    is_email_verified = int(request.json['is_email_verified'])
    password = request.json['password'].encode('ascii','ignore')
    pin = request.json['pin']
    photo = request.json['photo'].encode('ascii','ignore')



    user.user_id = user_id
    user.user_name = user_name
    user.name = name
    user.phone = phone
    user.is_otp_verified = is_otp_verified
    user.address_id = address_id
    user.email = email
    user.is_email_verified = is_email_verified
    user.password = password
    user.pin = pin
    user.photo = photo
 

    db.session.commit()
    return user_schema.jsonify(user)



# endpoint to delete user
@app.route("/deleteRegistration/<phone>", methods=["DELETE"])
def user_delete(phone):
    user = User.query.get(phone)
    db.session.delete(user)
    db.session.commit()

    return "True"

@app.route("/searchUser/<user_name>", methods=["GET"])
def searchUser(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    return user_schema.jsonify(user)


@app.route("/isUserNameAvail/<user_name>", methods=["GET"])
def isUserNameAvail(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    if (user==None):
        return "True"
    else:
        return "False"

@app.route("/doRequest", methods=["POST"])
def doRequest():

    request_info = request.json['request_info'].encode('ascii','ignore')
    user_id3 = int(request.json['user_id3'].encode('ascii','ignore'))
    user_id4 = int(request.json['user_id4'].encode('ascii','ignore'))
    request_status = request.json['request_status'].encode('ascii','ignore')

    new_request = Request(request_info, user_id3, user_id4, request_status)

    db.session.add(new_request)
    db.session.commit()
    return "True"


@app.route("/isRequestAccepted/<request_id>", methods=["GET"])
def isRequestAccepted(request_id):
    request = Request.query.get(request_id)
    return request_schema.jsonify(request.request_status)

@app.route("/doData", methods=["POST"])
def doData():

    data = request.json['data'].encode('ascii','ignore')
    data_title = request.json['data_title'].encode('ascii','ignore')
    user_id = int(request.json['user_id'].encode('ascii','ignore'))
    is_data_verified = request.json['is_data_verified']

    new_data = Data(data, data_title, user_id, is_data_verified)

    db.session.add(new_data)
    db.session.commit()
    return "True"

@app.route("/getData/<user_id>", methods=["GET"])
def getData(user_id):
    data = Data.query.filter_by(user_id=user_id).all()
    result = datas_schema.dump(data)
    return jsonify(a=result.data)

@app.route("/isDataVerified/<user_id>", methods=["GET"])
def isDataVerified(user_id):
    data = Data.query.filter_by(user_id=user_id).first()
    return data_schema.jsonify(data.is_data_verified)

@app.route("/doShareData", methods=["POST"])
def doShareData():

    user_id1 = request.json['user_id1'].encode('ascii','ignore')
    user_id2 = request.json['user_id2'].encode('ascii','ignore')
    data_id = int(request.json['data_id'])
    is_data_verified = request.json['is_data_verified']

    new_data = SharedData(user_id1, user_id2, data_id, is_data_verified)

    db.session.add(new_data)
    db.session.commit()
    return "True"

@app.route("/getDataId", methods=["GET"])
def getDataId():
    user_id = request.args['user_id']
    data_title = request.args['data_title'].encode('ascii','ignore')
    data = Data.query.filter_by(user_id=user_id, data_title=data_title).all()
    result = datas_schema.dump(data)
    return jsonify(a=result.data)







@app.route("/getShareData/<user_id1>", methods=["GET"])
def getShareData(user_id1):
    data = SharedData.query.filter_by(user_id1=user_id1).first()
    return shareddata_schema.jsonify(data)

@app.route("/doNotifications", methods=["POST"])
def doNotifications():

    notification_data = request.json['notification_data'].encode('ascii','ignore')
    user_id = request.json['user_id']

    new_data = Notifications(notification_data, user_id)

    db.session.add(new_data)
    db.session.commit()
    return "True"

@app.route("/notifications/<user_id>", methods=["GET"])
def notifications(user_id):
    data = Notifications.query.filter_by(user_id=user_id).first()
    return data_schema.jsonify(data)

@app.route("/postPackage", methods=["POST"])
def postPackage():

    package_data = request.json['package_data'].encode('ascii','ignore')
    package_title = request.json['package_title'].encode('ascii','ignore')
    package_price = request.json['package_price']

    new_data = Package(package_data, package_title, package_price)

    db.session.add(new_data)
    db.session.commit()
    return "True"

@app.route("/package/<package_id>", methods=["GET"])
def package(package_id):
    data = Package.query.get(package_id)
    return data_schema.jsonify(data)

@app.route("/deletePackage/<package_id>", methods=["DELETE"])
def package_delete(package_id):
    pack = Package.query.get(package_id)
    db.session.delete(pack)
    db.session.commit()

    return "True"

@app.route("/updatePackage/<package_id>", methods=["PUT"])
def updatePackage(package_id):
    Package.query.get(package_id)

    package_data = request.json['package_data'].encode('ascii','ignore')
    package_title = request.json['package_title'].encode('ascii','ignore')
    package_price = request.json['package_price']

    Package.package_data = package_data
    Package.package_title = package_title
    Package.package_price = package_price

    db.session.commit()
    return package_schema.jsonify(user)

@app.route("/postBooking", methods=["POST"])
def postBooking():

    data_dump = request.json['data_dump'].encode('ascii','ignore')
    user_id = request.json['user_id']
    package_id = request.json['package_id']
    amount = request.json['amount']
    total_amount = request.json['total_amount']
    is_paid = request.json['is_paid']
    is_delivered = request.json['is_delivered'].encode('ascii','ignore')
    booking_datetime = request.json['booking_datetime'].encode('ascii','ignore')

    new_data = Booking(data_dump, user_id, package_id, amount, total_amount, is_paid, is_delivered, booking_datetime)

    db.session.add(new_data)
    db.session.commit()
    return "True"

@app.route("/updateBooking/<booking_id>", methods=["PUT"])
def book_update(booking_id):
    booking = Booking.query.get(booking_id)

    data_dump = request.json['data_dump'].encode('ascii','ignore')
    user_id = request.json['user_id']
    package_id = request.json['package_id']
    amount = request.json['amount']
    total_amount = request.json['total_amount']
    is_paid = request.json['is_paid']
    is_delivered = request.json['is_delivered']
    booking_datetime = request.json['booking_datetime'].encode('ascii','ignore')

    booking.data_dump = data_dump
    booking.user_id = user_id
    booking.package_id = package_id
    booking.amount = amount
    booking.total_amount = total_amount
    booking.is_paid = is_paid
    booking.is_delivered = is_delivered
    booking.booking_datetime = booking_datetime 

    db.session.commit()
    return booking_schema.jsonify(booking)

@app.route("/getBookingOrders/<user_id>", methods=["GET"])
def getBookingOrders(user_id):
    data = Booking.query.filter_by(user_id=user_id).first()
    return booking_schema.jsonify(data)

@app.route("/getBookingOrdersId/<booking_id>", methods=["GET"])
def getBookingOrdersId(booking_id):
    data = Booking.query.filter_by(booking_id=booking_id).first()
    return booking_schema.jsonify(data)

@app.route("/getAllBookings", methods=["GET"])
def getAllBookings():
    data = Booking.query.all()
    result = bookings_schema.dump(data)
    return jsonify(a=result.data)


@app.route("/getAllUsers", methods=["GET"])
def getAllUsers():
    data = User.query.all()
    result = users_schema.dump(data)
    return jsonify(a=result.data)

@app.route("/getAllData", methods=["GET"])
def getAllData():
    data = Data.query.all()
    result = datas_schema.dump(data)
    return jsonify(a=result.data)

@app.route("/getAllPackages", methods=["GET"])
def getAllPackages():
    data = Package.query.all()
    result = packages_schema.dump(data)
    return jsonify(a=result.data)
# @app.route("/details", methods=["GET"])
# def get_details():
#     all_details = Details.query.all()
#     result = detailss_schema.dump(all_details)
#     return jsonify(a=result.data)


@app.route("/getAllPayment", methods=["GET"])
def getAllPayment():
    data = Payment.query.all()
    result = payments_schema.dump(data)
    return jsonify(a=result.data)

@app.route("/doPayment", methods=["POST"])
def doPayment():

    user_id = request.json['user_id']
    booking_id = request.json['booking_id']
    amount = request.json['amount']
    payment_mode = request.json['payment_mode']
    booking_datetime = request.json['booking_datetime'].encode('ascii', 'ignore')


    new_payment = Payment(user_id, booking_id, amount, payment_mode, booking_datetime)

    db.session.add(new_payment)
    db.session.commit()
    return "True"
@app.route("/getPackage/<package_id>", methods=["GET"])
def package_detail(package_id):
    package = Package.query.get(package_id)
    return package_schema.jsonify(package)

