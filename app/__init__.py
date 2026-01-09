from flask import Flask
from config import Config  # Ganti nama class menjadi 'Config'
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config) # Sesuaikan dengan nama class 'Config'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app.model.user import User
from app.model.dosen import Dosen
from app.model.mahasiswa import Mahasiswa