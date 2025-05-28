from . import db

class Bag(db.Model):
    __tablename__ = 'bags'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200))

    #Relationships
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    cart_items = db.relationship('CartItem', back_populates='bag', lazy=True)
    order_items = db.relationship('OrderItem', back_populates='bag', lazy=True)
    
    def __repr__(self):
        return f'<Bag {self.name}>' 