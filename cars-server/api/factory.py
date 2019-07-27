from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api

app = Flask(__name__)

app.config['MONGO_URI'] = ''
app.datebase = PyMongo(app)
app.cars_collection = app.datebase.db.cars

#Create API
api = Api(app)

