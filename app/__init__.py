from flask import Flask, request,jsonify, Blueprint
from app.blueprints import book_requests

def create_app():
    app = Flask(__name__)
    
    # add configs

    # blueprints
    app.register_blueprint(book_requests.get_blueprint())

    return app

