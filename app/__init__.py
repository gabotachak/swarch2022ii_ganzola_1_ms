"""Flask app creation."""
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect

from app.views import *
# from app.database import orm
from app.modules import *

# Active endpoints noted as following:
# (url_prefix, blueprint_object)
ACTIVE_ENDPOINTS = {
    "/ping": ping_view
}


def create_app(start_orm: bool = False):
    """Create Flask app."""

    load_dotenv()
    app = Flask(__name__)
    CORS(app)

    app.config["WTF_CSRF_CHECK_DEFAULT"] = False

    csrf = CSRFProtect()
    csrf.init_app(app)  # Compliant

    # accepts both /endpoint and /endpoint/ as valid URLs
    app.url_map.strict_slashes = False

    # register each active blueprint
    for endpoint in ACTIVE_ENDPOINTS:
        app.register_blueprint(ACTIVE_ENDPOINTS[endpoint], url_prefix=endpoint)

    # if start_orm:
    #     orm.start_mappers()

    return app
