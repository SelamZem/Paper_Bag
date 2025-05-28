from flask       import Blueprint, request, jsonify
from marshmallow import ValidationError
from app.repositories.user_repository import (
    list_users, get_user_by_id,
    get_user_by_username, register_user,
    authenticate_user, update_user,
    delete_user
)
from app.schemas.user_schema import (
    UserSchema, UserRegistrationSchema,
    UserLoginSchema
)
from app.services.auth_service import authenticate_and_generate_token
from app.utils import admin_required
from flask_jwt_extended import jwt_required

users_bp               = Blueprint('users', __name__, url_prefix='/users')
user_schema            = UserSchema()
users_schema           = UserSchema(many=True)
registration_schema    = UserRegistrationSchema()
login_schema           = UserLoginSchema()

@users_bp.route('/', methods=['GET'])
@admin_required
def list_all():
    return jsonify(users_schema.dump(list_users())), 200

@users_bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_one(user_id):
    return jsonify(user_schema.dump(get_user_by_id(user_id))), 200

@users_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        registration_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    user = register_user(data)
    return jsonify(user_schema.dump(user)), 201

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        login_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user, token = authenticate_and_generate_token(data['username'], data['password'])
    if not user:
        return jsonify({"msg": "Wrong username or Password"}), 401

    return jsonify(success=True,access_token=token, role=user.role, user=user_schema.dump(user)), 200

@users_bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update(user_id):
    data = request.get_json()
    try:
        user_schema.load(data, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400
    updated = update_user(user_id, data)
    return jsonify(user_schema.dump(updated)), 200

@users_bp.route('/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete(user_id):
    delete_user(user_id)
    return '', 204 