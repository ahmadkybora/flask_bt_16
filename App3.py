from flask_migrate import Migrate
from routes.panel.UserRoute import UserRoute
from config.database import db, app
from dataclasses import field
from email.policy import default
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import datetime
from flask_cors import CORS

from requests import request

app=Flask(__name__)
CORS(app)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)


## bot
## panel admin
app.register_blueprint(UserRoute, url_prefix='/users')

if __name__ == '__main__':
    app.debug = True
    app.run()