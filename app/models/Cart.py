from . import db

class Cart(db.Model):
    __tablename__ = 'carts'
    id = db.Column(db.Integer, primary_key=True)
     # Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    items = db.relationship('CartItem', backref='cart', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<Cart {self.id}>'
        
    @property
    def total_price(self):
        return sum(item.total_price for item in self.items) 