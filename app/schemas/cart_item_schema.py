from app.schemas import ma
from marshmallow import fields

class CartItemSchema(ma.Schema):
    id       = fields.Int(dump_only=True)
    cart_id  = fields.Int(required=True)
    bag_id   = fields.Int(required=True)
    quantity = fields.Int(required=True)