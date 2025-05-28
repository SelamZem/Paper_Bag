from app.schemas import ma
from marshmallow import fields, validate

class UserSchema(ma.Schema):
    id         = fields.Int(dump_only=True)
    username   = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    email      = fields.Email(required=True)
    first_name = fields.Str(allow_none=True)
    last_name  = fields.Str(allow_none=True)
    phone      = fields.Str(allow_none=True)
    address    = fields.Str(allow_none=True)
    role       = fields.Str(dump_only=True)

class UserRegistrationSchema(ma.Schema):
    username   = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    email      = fields.Email(required=True)
    password   = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))
    first_name = fields.Str()
    last_name  = fields.Str()
    phone      = fields.Str()
    address    = fields.Str()
    #role       = fields.Str()

class UserLoginSchema(ma.Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)