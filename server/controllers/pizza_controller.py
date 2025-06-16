from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint("pizza_bp", __name__, url_prefix="/pizzas")

@pizza_bp.route("/", methods=["GET"])
def get_pizzas():
    pizzas = Pizza.query.all()
    response = [pizza.to_dict() for pizza in pizzas]
    return jsonify(response), 200

