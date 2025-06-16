from server.models import db, Restaurant, Pizza, RestaurantPizza
from server.app import create_app

app = create_app()

with app.app_context():
    # Clear existing data
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    # Create restaurants
    r1 = Restaurant(name="Mario's Pizza", address="123 Main St")
    r2 = Restaurant(name="Kiki's Pizza", address="456 Elm St")

    # Create pizzas
    p1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Mozzarella")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Create RestaurantPizza (join table entries)
    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    rp3 = RestaurantPizza(price=15, restaurant=r2, pizza=p1)

    # Add to session and commit
    db.session.add_all([r1, r2, p1, p2, rp1, rp2, rp3])
    db.session.commit()

    print("✅ Database seeded!")
