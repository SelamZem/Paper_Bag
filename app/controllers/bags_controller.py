from flask           import Blueprint, request, jsonify
from marshmallow     import ValidationError
from app.repositories.bag_repository import (
    list_bags,
    get_bag_by_id,
    list_bags_by_category,
    list_available_bags,
    search_bags,
    create_bag,
    update_bag,
    delete_bag
)
from app.schemas.bag_schema import BagSchema
from app.services.auth_service import authenticate_and_generate_token
from app.utils import admin_required

bags_bp      = Blueprint('bags', __name__, url_prefix='/bags')
bag_schema   = BagSchema()
bags_schema  = BagSchema(many=True)

@bags_bp.route('/', methods=['GET'])
def list_all_bags():
    return jsonify(bags_schema.dump(list_bags())), 200

@bags_bp.route('/<int:bag_id>', methods=['GET'])
def get_single_bag(bag_id):
    return jsonify(bag_schema.dump(get_bag_by_id(bag_id))), 200

@bags_bp.route('/category/<int:category_id>', methods=['GET'])
def get_by_category(category_id):
    return jsonify(bags_schema.dump(list_bags_by_category(category_id))), 200

@bags_bp.route('/available', methods=['GET'])
def get_available():
    return jsonify(bags_schema.dump(list_available_bags())), 200

@bags_bp.route('/search', methods=['GET'])
def search():
    q = request.args.get('q', '')
    return jsonify(bags_schema.dump(search_bags(q))), 200

@bags_bp.route('/', methods=['POST'])
@admin_required
def create():
    data = request.get_json()
    try:
        bag_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    new_bag = create_bag(data)
    return jsonify(bag_schema.dump(new_bag)), 201

@bags_bp.route('/<int:bag_id>', methods=['PUT'])
@admin_required
def update(bag_id):
    data = request.get_json()
    try:
        bag_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_bag(bag_id, data)
    return jsonify(bag_schema.dump(updated)), 200

@bags_bp.route('/<int:bag_id>', methods=['DELETE'])
@admin_required
def delete(bag_id):
    delete_bag(bag_id)
    return '', 204 