import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql://root:admin@localhost/builder'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
