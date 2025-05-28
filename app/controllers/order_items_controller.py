from flask             import Blueprint, request, jsonify
from marshmallow       import ValidationError
from app.repositories.order_item_repository  import (
    list_order_items, get_order_item_by_id,
    list_order_items_for_order,
    create_order_item, update_order_item,
    delete_order_item
)
from app.schemas.order_item_schema import OrderItemSchema

order_items_bp      = Blueprint('order_items', __name__, url_prefix='/order-items')
order_item_schema   = OrderItemSchema()
order_items_schema  = OrderItemSchema(many=True)

@order_items_bp.route('/', methods=['GET'])
def list_all():
    return jsonify(order_items_schema.dump(list_order_items())), 200

@order_items_bp.route('/<int:item_id>', methods=['GET'])
def get_one(item_id):
    return jsonify(order_item_schema.dump(get_order_item_by_id(item_id))), 200

@order_items_bp.route('/order/<int:order_id>', methods=['GET'])
def list_for_order(order_id):
    return jsonify(order_items_schema.dump(list_order_items_for_order(order_id))), 200

@order_items_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    try:
        order_item_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    item = create_order_item(data)
    return jsonify(order_item_schema.dump(item)), 201

@order_items_bp.route('/<int:item_id>', methods=['PUT'])
def update(item_id):
    data = request.get_json()
    try:
        order_item_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_order_item(item_id, data)
    return jsonify(order_item_schema.dump(updated)), 200

@order_items_bp.route('/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    delete_order_item(item_id)
    return '', 204 