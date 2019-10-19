from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:30111998a@127.0.0.1/falcons?host=127.0.0.1?port=3306' + os.path.join(basedir, 'main')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from main import route



