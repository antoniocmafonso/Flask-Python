from flask import Blueprint, jsonify, request
from bd import items

items_blueprint = Blueprint('items', __name__)

# Rota para obter todos os itens
@items_blueprint.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Rota para obter um item específico por ID
@items_blueprint.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404
