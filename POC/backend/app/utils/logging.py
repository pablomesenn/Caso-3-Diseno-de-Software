import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime

# Setup structured logging
logger = logging.getLogger('DataPuraVida')
log_handler = logging.StreamHandler()
log_handler.setFormatter(jsonlogger.JsonFormatter())
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

def log_request(endpoint, user, status):
    logger.info({
        'endpoint': endpoint,
        'user': user,
        'status': status,
        'timestamp': datetime.utcnow().isoformat()
    })