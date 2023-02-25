import os
from .base import db

def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/test.db')
    db.init_app(app)
