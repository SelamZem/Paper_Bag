from app.schemas import ma
from marshmallow import fields
from .cart_item_schema import CartItemSchema

class CartSchema(ma.Schema):
    id      = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    items   = fields.Nested(CartItemSchema, many=True)