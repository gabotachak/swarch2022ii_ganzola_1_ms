from marshmallow import Schema, fields, ValidationError, post_load
from marshmallow.validate import Range, Length, Regexp

from app import models


class SearchTransaction(Schema):
    id_transaction = fields.Int(validate=Range(min=1, error="id cannot be negative"))
    sender = fields.Str(
        validate=[Length(min=1, max=20), Regexp(r"^(\d+|[a-zA-Z]+){1}$", error="id or username not valid")]
    )
    receiver = fields.Str(
        validate=[Length(min=1, max=20), Regexp(r"^(\d+|[a-zA-Z]+){1}$", error="id or username not valid")]
    )
    transaction_time = fields.DateTime()

    @post_load
    def make(self, data, **kwargs):
        if not data:
            raise ValidationError("No params provided")

        return {k: v for k, v in models.Transaction(**data).to_dict().items() if v is not None}


class CreateTransaction(Schema):
    sender = fields.Str(
        validate=[Length(min=1, max=20), Regexp(r"^(\d+|[a-zA-Z]+){1}$", error="id or username not valid")]
    )
    receiver = fields.Str(
        validate=[Length(min=1, max=20), Regexp(r"^(\d+|[a-zA-Z]+){1}$", error="id or username not valid")]
    )
    amount = fields.Float(validate=Range(min=1, error="amount cannot be negative"))

    @post_load
    def make(self, data, **kwargs):
        return models.Transaction(**data)
