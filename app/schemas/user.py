from marshmallow import Schema, fields, post_load, ValidationError
from marshmallow.validate import Length, Range

from app import models
from app.utils.log import logger


class SearchUser(Schema):
    id_user = fields.Int(validate=Range(min=1, error="id cannot be negative"))
    username = fields.Str(validate=Length(min=1, max=20))

    @post_load
    def make(self, data, **kwargs):
        if not data:
            raise ValidationError("No params provided")

        return {k: v for k, v in models.User(**data).to_dict().items() if v is not None}
