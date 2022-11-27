from functools import wraps
from http import HTTPStatus

from flask import jsonify
from marshmallow import ValidationError

from app.exceptions import NotFoundException, AlreadyExistsException
from app.utils.log import logger
from app.utils.constants import *


def error_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as ve:
            logger.error(f"{ve.__class__.__name__}: {ve}")
            return (
                jsonify({ERROR_RESPONSE: f"Invalid JSON format ({ve})"}),
                HTTPStatus.BAD_REQUEST,
            )
        except NotFoundException as nfe:
            logger.error(f"{nfe.__class__.__name__}")
            return (
                jsonify({ERROR_RESPONSE: f"{nfe.resource} ({nfe.resource_id}) not found"}),
                HTTPStatus.NOT_FOUND,
            )
        except AlreadyExistsException as aee:
            logger.error(f"{aee.__class__.__name__}")
            return (
                jsonify({ERROR_RESPONSE: f"{aee.resource} ({aee.resource_id}) already exists"}),
                HTTPStatus.CONFLICT,
            )

    return wrapper
