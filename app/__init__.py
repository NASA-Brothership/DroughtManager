from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes

    from app.plants import plants_bp
    from app.soil_moisture import soil_moisture_bp

    app.register_blueprint(plants_bp)
    app.register_blueprint(soil_moisture_bp)

    return app
