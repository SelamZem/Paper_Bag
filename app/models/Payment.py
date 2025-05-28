from . import db
from datetime import datetime
from enum import Enum

class PaymentStatus(Enum):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    FAILED = 'Failed'
    CANCELLED = 'Cancelled'

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.Enum(PaymentStatus), default=PaymentStatus.PENDING)
    transaction_id = db.Column(db.String(100), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship
    order = db.relationship('Order', backref='payment_order', uselist=False)

    def __repr__(self):
        return f'<Payment {self.id} - Order {self.order_id}>'
