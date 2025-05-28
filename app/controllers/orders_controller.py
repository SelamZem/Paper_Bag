from flask       import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.repositories.order_repository import (
    list_orders, get_order_by_id,
    list_orders_by_user, list_orders_by_date_range,
    create_order, update_order, delete_order
)
from app.schemas.order_schema import OrderSchema
from flask_jwt_extended import jwt_required

orders_bp     = Blueprint('orders', __name__, url_prefix='/api/orders')
order_schema  = OrderSchema()
orders_schema = OrderSchema(many=True)
from app.utils import admin_required

@orders_bp.route('/', methods=['GET'])
@admin_required
def list_all():
    return jsonify(orders_schema.dump(list_orders())), 200

@orders_bp.route('/<int:order_id>', methods=['GET'])
@jwt_required()
def get_one(order_id):
    return jsonify(order_schema.dump(get_order_by_id(order_id))), 200

@orders_bp.route('/user/<int:user_id>', methods=['GET'])
def by_user(user_id):
    return jsonify(orders_schema.dump(list_orders_by_user(user_id))), 200

@orders_bp.route('/filter', methods=['GET'])
def by_date():
    start = request.args.get('start')
    end   = request.args.get('end')
    return jsonify(orders_schema.dump(list_orders_by_date_range(start, end))), 200

@orders_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    try:
        order_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    new_order = create_order(data)
    return jsonify(order_schema.dump(new_order)), 201

@orders_bp.route('/<int:order_id>', methods=['PUT'])
@jwt_required()
def update(order_id):
    data = request.get_json()
    try:
        order_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_order(order_id, data)
    return jsonify(order_schema.dump(updated)), 200

@orders_bp.route('/<int:order_id>', methods=['DELETE'])
@jwt_required()
def delete(order_id):
    delete_order(order_id)
    return '', 204 