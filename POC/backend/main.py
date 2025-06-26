from flask import Flask
from flask_cors import CORS
from app.handlers.secure_data import secure_data_bp
from app.handlers.data import data_bp

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Register blueprints
app.register_blueprint(secure_data_bp, url_prefix='/api')
app.register_blueprint(data_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)