from app.schemas import ma
from marshmallow import fields, validate

class BagSchema(ma.Schema):
    id             = fields.Int(dump_only=True)
    name           = fields.Str(required=True, validate=validate.Length(max=100))
    description    = fields.Str(allow_none=True)
    price          = fields.Float(required=True)
    stock_quantity = fields.Int(required=True)
    image_url      = fields.Url(allow_none=True)
    category_id    = fields.Int(required=True)