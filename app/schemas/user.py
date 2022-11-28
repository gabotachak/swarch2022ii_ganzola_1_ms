from marshmallow import Schema, fields, post_load, ValidationError

from app import models


class SearchUser(Schema):
    id_user = fields.Int()
    first_name = fields.Str(min_length=1, max_length=45)
    last_name = fields.Str(min_length=1, max_length=45)
    username = fields.Str(min_length=1, max_length=20)

    @post_load
    def make(self, data, **kwargs):
        if not data:
            raise ValidationError("No params provided")

        return {k: v for k, v in models.User(**data).to_dict().items() if v is not None}
