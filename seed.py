from app import create_app
from app.models import db
from app.models.Category import Category
from app.models.Bag import Bag
from app.models.User import User
from app.models.Cart import Cart
from app.models.CartItem import CartItem
from app.models.Order import Order
from app.models.OrderItem import OrderItem
from app.models.Payment import Payment, PaymentStatus

app = create_app()
def seed():
    with app.app_context():
       
        db.drop_all()
        db.create_all()

        cat1 = Category(name="Small", description="Small bags for everyday use")
        cat2 = Category(name="Medium1", description="Medium bags for shopping")
        cat3 = Category(name="Medium2", description="Medium bags for travel")
        cat4 = Category(name="Large", description="Large bags for travel and storage")
        db.session.add_all([cat1, cat2])
        db.session.commit()

        bag1 = Bag(
            name="Eco Green Bag",
            description="Eco bag made of hemp",
            price=5.99,
            stock_quantity=20,
            image_url="eco1.jpg",
            category_id=cat1.id
        )
        bag2 = Bag(
            name="Luxury Gift Bag",
            description="Silky red gift bag",
            price=9.99,
            stock_quantity=10,
            image_url="gift1.jpg",
            category_id=cat2.id
        )
        db.session.add_all([bag1, bag2])
        db.session.commit()

        user2 = User(
            username="abc123",
            email="selam@gmail.com",
            first_name="abc",
            last_name="Tester",
            phone="1234567890",
            address="123 Test Street",
            role="Admin"
        )
        user2.set_password("test1234")
        db.session.add(user2)
        db.session.commit()
    
        user1 = User(
            username="pis123",
            email="pis@example.com",
            first_name="Pis",
            last_name="Tester",
            phone="1234567890",
            address="123 Test Street"
        )
        user1.set_password("test1234")
        db.session.add(user1)
        db.session.commit()

        cart = Cart(user_id=user1.id)
        db.session.add(cart)
        db.session.commit()

    
        cart_item1 = CartItem(cart_id=cart.id, bag_id=bag1.id, quantity=2)
        cart_item2 = CartItem(cart_id=cart.id, bag_id=bag2.id, quantity=1)
        db.session.add_all([cart_item1, cart_item2])
        db.session.commit()

        
        order = Order(
            user_id=user1.id,
            total_amount=bag1.price * 2 + bag2.price
        )
        db.session.add(order)
        db.session.commit()

        
        order_item1 = OrderItem(order_id=order.id, bag_id=bag1.id, quantity=2)
        order_item2 = OrderItem(order_id=order.id, bag_id=bag2.id, quantity=1)
        db.session.add_all([order_item1, order_item2])
        db.session.commit()

        
        payment = Payment(
            order_id=order.id,
            amount=order.total_amount,
            status=PaymentStatus.COMPLETED,
            transaction_id="TXN123456"
        )
        db.session.add(payment)
        db.session.commit()

        print(" Database seeded successfully!")


if __name__ == "__main__":
    seed()
