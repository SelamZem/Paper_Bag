from functools import wraps
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
from app.repositories.user_repository import get_user_by_id

def admin_required(fn):
    @wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user_id = get_jwt_identity()
        user = get_user_by_id(user_id)
        if not user or user.role != 'Admin':
            return jsonify({"msg": "Admins only!"}), 403
        return fn(*args, **kwargs)
    return wrapper
