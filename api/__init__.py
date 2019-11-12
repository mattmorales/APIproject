from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

import common.config

api = Api(app)
ma = Marshmallow(app)
db = SQLAlchemy(app)

import api.movies
import api.admin
import api.accounts
