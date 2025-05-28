from flask          import Blueprint, request, jsonify
from marshmallow    import ValidationError
from app.repositories.cart_repository import (
    list_carts, get_cart_by_id, get_cart_by_user,
    create_cart, update_cart, delete_cart
)
from app.schemas.cart_schema import CartSchema
from app.utils import admin_required

carts_bp     = Blueprint('carts', __name__, url_prefix='/carts')
cart_schema  = CartSchema()
carts_schema = CartSchema(many=True)

@carts_bp.route('/', methods=['GET'])
@admin_required
def list_all():
    return jsonify(carts_schema.dump(list_carts())), 200

@carts_bp.route('/<int:cart_id>', methods=['GET'])
def get_one(cart_id):
    return jsonify(cart_schema.dump(get_cart_by_id(cart_id))), 200

@carts_bp.route('/user/<int:user_id>', methods=['GET'])
def get_by_user(user_id):
    return jsonify(cart_schema.dump(get_cart_by_user(user_id))), 200

@carts_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    try:
        cart_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    cart = create_cart(data)
    return jsonify(cart_schema.dump(cart)), 201

@carts_bp.route('/<int:cart_id>', methods=['PUT'])
def update(cart_id):
    data = request.get_json()
    try:
        cart_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_cart(cart_id, data)
    return jsonify(cart_schema.dump(updated)), 200

@carts_bp.route('/<int:cart_id>', methods=['DELETE'])
def delete(cart_id):
    delete_cart(cart_id)
    return '', 204 