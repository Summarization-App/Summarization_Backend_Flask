from app import app
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound

hostedApp = Flask(__name__)

hostedApp.wsgi_app = DispatcherMiddleware(NotFound(), {"/flask": app})


if __name__ == "__main__":
    # Giving the predefined url and using the Middleware to do that
    hostedApp.run()
