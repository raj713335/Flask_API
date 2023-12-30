from marshmallow import Schema, fields

from schemas_new.itemSchema import PlainItemSchema, ItemSchema
from schemas_new.storeSchema import PlainStoreSchema


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class TagsSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagsSchema)

