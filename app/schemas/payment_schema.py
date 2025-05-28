from app.schemas import ma
from marshmallow import fields

class PaymentSchema(ma.Schema):
    id             = fields.Int(dump_only=True)
    order_id       = fields.Int(required=True)
    amount         = fields.Float(required=True)
    status         = fields.Str(dump_only=True)
    transaction_id = fields.Str(allow_none=True)
    created_at     = fields.DateTime(dump_only=True)