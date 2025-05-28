from flask            import Blueprint, request, jsonify
from marshmallow      import ValidationError
from app.repositories.category_repository import (
    list_categories, get_category_by_id,
    list_bags_for_category,
    create_category, update_category,
    delete_category
)
from app.schemas.category_schema import CategorySchema
from app.schemas.bag_schema      import BagSchema
from app.utils import admin_required

categories_bp     = Blueprint('categories', __name__, url_prefix='/categories')
category_schema   = CategorySchema()
categories_schema = CategorySchema(many=True)
bag_schema        = BagSchema()
bags_schema       = BagSchema(many=True)

@categories_bp.route('/', methods=['GET'])
def list_all_categories():
    return jsonify(categories_schema.dump(list_categories())), 200

@categories_bp.route('/<int:cat_id>', methods=['GET'])
def get_category(cat_id):
    return jsonify(category_schema.dump(get_category_by_id(cat_id))), 200

@categories_bp.route('/<int:cat_id>/bags', methods=['GET'])
def bags_in_category(cat_id):
    return jsonify(bags_schema.dump(list_bags_for_category(cat_id))), 200

@categories_bp.route('/', methods=['POST'])
@admin_required
def create():
    data = request.get_json()
    try:
        category_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    new_cat = create_category(data)
    return jsonify(category_schema.dump(new_cat)), 201

@categories_bp.route('/<int:cat_id>', methods=['PUT'])
@admin_required
def update(cat_id):
    data = request.get_json()
    try:
        category_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_category(cat_id, data)
    return jsonify(category_schema.dump(updated)), 200

@categories_bp.route('/<int:cat_id>', methods=['DELETE'])
@admin_required
def delete(cat_id):
    delete_category(cat_id)
    return '', 204 