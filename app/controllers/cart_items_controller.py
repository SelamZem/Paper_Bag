from flask             import Blueprint, request, jsonify
from marshmallow       import ValidationError
from app.repositories.cart_item_repository  import (
    list_cart_items, get_cart_item_by_id,
    list_cart_items_for_cart,
    create_cart_item, update_cart_item,
    delete_cart_item
)
from app.schemas.cart_item_schema import CartItemSchema

cart_items_bp      = Blueprint('cart_items', __name__, url_prefix='/cart-items')
cart_item_schema   = CartItemSchema()
cart_items_schema  = CartItemSchema(many=True)

@cart_items_bp.route('/', methods=['GET'])
def list_all():
    return jsonify(cart_items_schema.dump(list_cart_items())), 200

@cart_items_bp.route('/<int:item_id>', methods=['GET'])
def get_one(item_id):
    return jsonify(cart_item_schema.dump(get_cart_item_by_id(item_id))), 200

@cart_items_bp.route('/cart/<int:cart_id>', methods=['GET'])
def list_for_cart(cart_id):
    return jsonify(cart_items_schema.dump(list_cart_items_for_cart(cart_id))), 200

@cart_items_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    try:
        cart_item_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    item = create_cart_item(data)
    return jsonify(cart_item_schema.dump(item)), 201

@cart_items_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id):
    data = request.get_json()
    try:
        cart_item_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_cart_item(item_id, data)
    return jsonify(cart_item_schema.dump(updated)), 200

@cart_items_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    delete_cart_item(item_id)
    return '', 204 