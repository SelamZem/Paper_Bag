from app.schemas import ma
from marshmallow import fields, validate

class CategorySchema(ma.Schema):
    id          = fields.Int(dump_only=True)
    name        = fields.Str(required=True, validate=validate.Length(max=50))
    description = fields.Str(allow_none=True, validate=validate.Length(max=200))