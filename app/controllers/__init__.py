from .bags_controller        import bags_bp
from .categories_controller  import categories_bp
from .cart_items_controller  import cart_items_bp
from .carts_controller       import carts_bp
from .order_items_controller import order_items_bp
from .orders_controller      import orders_bp
from .payments_controller    import payments_bp
from .users_controller       import users_bp

blueprints = [
    bags_bp,
    categories_bp,
    cart_items_bp,
    carts_bp,
    order_items_bp,
    orders_bp,
    payments_bp,
    users_bp,
]