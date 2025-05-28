from flask       import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.repositories.payment_repository import (
    list_payments, get_payment_by_id,
    list_payments_by_order, list_payments_by_status,
    create_payment, update_payment, delete_payment
)
from app.schemas.payment_schema import PaymentSchema
from app.utils import admin_required
from flask_jwt_extended import jwt_required

payments_bp      = Blueprint('payments', __name__, url_prefix='/payments')
payment_schema   = PaymentSchema()
payments_schema  = PaymentSchema(many=True)

@payments_bp.route('/', methods=['GET'])
@admin_required
def list_all():
    return jsonify(payments_schema.dump(list_payments())), 200

@payments_bp.route('/<int:pay_id>', methods=['GET'])
@jwt_required()
def get_one(pay_id):
    return jsonify(payment_schema.dump(get_payment_by_id(pay_id))), 200

@payments_bp.route('/order/<int:order_id>', methods=['GET'])
@jwt_required()
def by_order(order_id):
    return jsonify(payments_schema.dump(list_payments_by_order(order_id))), 200

@payments_bp.route('/status/<status>', methods=['GET'])
@jwt_required()
def by_status(status):
    return jsonify(payments_schema.dump(list_payments_by_status(status))), 200

@payments_bp.route('/', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()
    try:
        payment_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    pay = create_payment(data)
    return jsonify(payment_schema.dump(pay)), 201

@payments_bp.route('/<int:pay_id>', methods=['PUT'])
@jwt_required()
def update(pay_id):
    data = request.get_json()
    try:
        payment_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_payment(pay_id, data)
    return jsonify(payment_schema.dump(updated)), 200

@payments_bp.route('/<int:pay_id>', methods=['DELETE'])
@jwt_required()
def delete(pay_id):
    delete_payment(pay_id)
    return '', 204 