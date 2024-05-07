import os
from flask import Flask, request,jsonify, Blueprint
from app.blueprints import book_requests
# from pymongo import MongoClient


def create_app():

    app = Flask(__name__)
    
    # add configs
    config_type = os.getenv('CONFIG_TYPE', default='config.ProcConfig')
    app.config.from_object(config_type)

    # # database init
    # db_client = MongoClient(app.config['DB_ACCESS'])
    # database = db_client['DB_NAME']
    @app.after_request
    def add_header(response):
        response.headers['Content-Security-Policy'] = "sandbox; default-src 'self'; frame-ancestors 'none'"
        response.headers['Strict-Transport-Security'] = "max-age=31536000; includeSubDomains"
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        
        return response
    # blueprints
    app.register_blueprint(book_requests.get_blueprint())

    return app
