from flask import Blueprint, jsonify, request
from bd import items

aad_blueprint = Blueprint('aad', __name__)

# Rota para adicionar um novo item
@aad_blueprint.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
@aad_blueprint.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        updated_data = request.json
        item.update(updated_data)
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Rota para deletar um item
@aad_blueprint.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})
