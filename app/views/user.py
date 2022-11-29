"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app import schemas
from app.utils.decorators import error_decorator
from app.utils.constants import PING_RESPONSE

user_view = Blueprint("user", __name__)


@user_view.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""

    return jsonify(PING_RESPONSE), HTTPStatus.OK


@user_view.route("/", methods=["GET"])
@error_decorator
def get_user_by_params():
    """Get user by query params."""

    params = schemas.SearchUser().load(request.args)
    res = app.user_controller.search_user(params)

    return jsonify(res), HTTPStatus.OK


@user_view.route("/", methods=["POST"])
@error_decorator
def create_user():
    """Create user."""

    user = schemas.CreateUser().load(request.json)
    res = app.user_controller.create_user(user)

    return jsonify(res), HTTPStatus.CREATED
