from . import db
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200))
    role = db.Column(db.String(20), default='customer')
    
    # Relationships
    orders = db.relationship('Order', backref='user', lazy=True)
    cart = db.relationship('Cart', backref='user', uselist=False, lazy=True)
    
    def __repr__(self):
        return f'<User {self.username}>' 
    def set_password(self, plaintext: str):
        self.password_hash = generate_password_hash(plaintext)

    def verify_password(self, plaintext: str) -> bool:
        return check_password_hash(self.password_hash, plaintext)