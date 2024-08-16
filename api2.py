from flask import Flask, jsonify, request
from bd import items

app = Flask(__name__)

# Rota para obter todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Rota para obter um item específico por ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Rota para adicionar um novo item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        updated_data = request.json
        item.update(updated_data)
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# Rota para deletar um item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)
