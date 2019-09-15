from marshmallow import Schema, fields
from bson import ObjectId

from core.exceptions import InvalidArgumentException

Schema.TYPE_MAPPING[ObjectId] = fields.String


class BaseSchema(Schema):
    class Meta(Schema.Meta):
        strict = True

    def handle_error(self, error, data, *, many, **kwargs):
        raise InvalidArgumentException(error.messages)


class MsgSchema(BaseSchema):

    nick = fields.String(allow_none=True)
    avatar = fields.String(allow_none=True)
    msg = fields.String(required=True)

    # dump-only
    _id = fields.String(dump_only=True)
    create_t = fields.Float(dump_only=True)
    user_id = fields.String(dump_only=True)


class UserSchema(BaseSchema):

    _id = fields.String(dump_only=True)
    nick = fields.String(dump_only=True)
    avatar = fields.String(dump_only=True)
