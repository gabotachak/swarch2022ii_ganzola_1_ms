"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

from app.utils.decorators import error_decorator
from app.utils.constants import PING_RESPONSE

ping_view = Blueprint("ping", __name__)


@ping_view.route("/", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""

    return jsonify(PING_RESPONSE), HTTPStatus.OK
