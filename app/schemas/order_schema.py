from app.schemas import ma
from marshmallow import fields
from .order_item_schema import OrderItemSchema

class OrderSchema(ma.Schema):
    id           = fields.Int(dump_only=True)
    user_id      = fields.Int(required=True)
    total_amount = fields.Float(dump_only=True)
    created_at   = fields.DateTime(dump_only=True)
    order_items  = fields.Nested(OrderItemSchema, many=True)