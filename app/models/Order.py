from . import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    order_items = db.relationship('OrderItem', backref='order', lazy=True) 
    payments = db.relationship('Payment', backref='order_reference', lazy=True)
    
    def __repr__(self):
        return f'<Order {self.id} - User {self.user_id}>'

    @property
    def total_amount_calculated(self):
        return sum(item.price * item.quantity for item in self.order_items)
