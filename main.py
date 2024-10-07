from app.analysis import analyze_drought
from app.plants import plants_bp
from app.wbi import wbi_bp

from flask import Flask, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(plants_bp)
app.register_blueprint(wbi_bp)

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/forms')
def serve_forms():
    return send_from_directory('static', 'forms.html')

@app.route('/satellite')
def serve_satellite():
    return send_from_directory('static', 'satellite.html')

@app.route("/drought-analysis", methods=["POST"])
def drought_analysis_route():
    data_input = {
        "crop_type": request.json.get('crop_type'),
        "latitude": request.json.get('latitude'),
        "longitude": request.json.get('longitude'),
        "radius_km": request.json.get('radius_km'),
        "is_irrigated": request.json.get('is_irrigated'),
        "planting_period": request.json.get('planting_period'),
        "existing_crops": request.json.get('existing_crops')
    }
    return analyze_drought(data_input)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
