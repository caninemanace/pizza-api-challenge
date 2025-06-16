from flask import Blueprint, jsonify
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint("restaurant_bp", __name__, url_prefix="/restaurants")

@restaurant_bp.route("/", methods=["GET"])
def get_restaurants():
    restaurants = Restaurant.query.all()
    response = [restaurant.to_dict() for restaurant in restaurants]
    return jsonify(response), 200

