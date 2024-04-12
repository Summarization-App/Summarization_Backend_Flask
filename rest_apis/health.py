from flask import Blueprint


health = Blueprint('health', __name__)


@health.route("/health",  methods=["GET"])
def healthz():
    message = {
        'status': 'healthy'
    }
    return message, 200
