from flask_jwt_extended import create_access_token
from app.repositories.user_repository import get_user_by_username

def authenticate_and_generate_token(username, password):
    user = get_user_by_username(username)
    if not user or not user.verify_password(password):
        return None, None
    token = create_access_token(identity=str(user.id))

    return user, token
