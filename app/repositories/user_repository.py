from typing import List
from flask import abort
from app.models import db
from app.models.User import User

def list_users() -> List[User]:
    return User.query.all()

def get_user_by_id(user_id: int) -> User:
    user = User.query.get(user_id)
    if not user:
        abort(404, f"User {user_id} not found")
    return user

def get_user_by_username(username: str) -> User:
    user = User.query.filter_by(username=username).first()
    if not user:
        abort(404, f"User '{username}' not found")
    return user

def create_user(data: dict) -> User:
    user = User(
        username   = data['username'],
        email      = data['email'],
        first_name = data['first_name'],
        last_name  = data['last_name'],
        phone      = data['phone'],
        address    = data.get('address'),
        role       = data.get('role', 'customer')
    )
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return user

def update_user(user_id: int, data: dict) -> User:
    user = get_user_by_id(user_id)
    if 'password' in data:
        user.set_password(data.pop('password'))
    for key, value in data.items():
        setattr(user, key, value)
    db.session.commit()
    return user

def delete_user(user_id: int) -> None:
    user = get_user_by_id(user_id)
    db.session.delete(user)
    db.session.commit()

def register_user(data: dict) -> User:
    return create_user(data)

def authenticate_user(username: str, password: str) -> User:
    user = get_user_by_username(username)
    if not user.verify_password(password):
        abort(401, "Invalid credentials")
    return user