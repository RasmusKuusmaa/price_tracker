import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///price_tracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False