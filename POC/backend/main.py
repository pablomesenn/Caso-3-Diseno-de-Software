from flask import Flask
from flask_cors import CORS
from app.handlers.secure_data import secure_data_bp
from app.handlers.data import data_bp
from app.config.config import OKTA_ISSUER, API_AUDIENCE
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging
from datetime import datetime
import json
import boto3

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Setup structured logging
logger = logging.getLogger('DataPuraVida')
log_handler = logging.StreamHandler()
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# Initialize CloudWatch client
cloudwatch = boto3.client('logs')

def log_request(endpoint, user, status):
    logger.info({
        'endpoint': endpoint,
        'user': user,
        'status': status,
        'timestamp': datetime.utcnow().isoformat()
    })
    cloudwatch.put_log_events(
        logGroupName='DataPuraVidaLogs',
        logStreamName='API',
        logEvents=[{
            'timestamp': int(datetime.utcnow().timestamp() * 1000),
            'message': json.dumps({'endpoint': endpoint, 'user': user, 'status': status})
        }]
    )

# Rate limiting
limiter = Limiter(app, key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])

# Register blueprints
app.register_blueprint(secure_data_bp, url_prefix='/api')
app.register_blueprint(data_bp, url_prefix='/api')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)