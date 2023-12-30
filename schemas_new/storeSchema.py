from marshmallow import Schema, fields

from schemas_new.itemSchema import PlainItemSchema
from schemas_new.tagSchema import PlainTagSchema


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)

