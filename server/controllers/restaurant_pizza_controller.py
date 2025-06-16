from flask import Blueprint, request, jsonify
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza
from server.models import db

restaurant_pizza_bp = Blueprint("restaurant_pizza_bp", __name__, url_prefix="/restaurant_pizzas")

@restaurant_pizza_bp.route("/", methods=["POST"])
def create_restaurant_pizza():
    data = request.get_json()

    try:
        price = int(data["price"])
        if not (1 <= price <= 30):
            return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

        new_rp = RestaurantPizza(
            price=price,
            restaurant_id=data["restaurant_id"],
            pizza_id=data["pizza_id"]
        )
        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.get(data["pizza_id"])
        return jsonify(pizza.to_dict()), 201

    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
    


