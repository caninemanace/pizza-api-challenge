from flask import Blueprint, jsonify
from server.models.restaurant import Restaurant
from server.models import db
from server.models.restaurant_pizza import RestaurantPizza

restaurant_bp = Blueprint("restaurant_bp", __name__, url_prefix="/restaurants")

@restaurant_bp.route("/", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    response = [restaurant.to_dict() for restaurant in restaurants]
    return jsonify(response), 200

@restaurant_bp.route("/<int:id>", methods=["DELETE"])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    # Delete associated RestaurantPizzas first (if cascade not set)
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()

    db.session.delete(restaurant)
    db.session.commit()

    return '', 204

