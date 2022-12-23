import os
from flask import Flask
from db import db
from serialization import ma
from api import api_bp
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("VT_BAGLANTI")

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(api_bp, url_prefix="/api")

CORS(app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run()
