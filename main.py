from flask import Flask, Blueprint
from items.items_bp import items_blueprint
from aad.aad_bp import aad_blueprint

app = Flask(__name__)

# Registrar a blueprint
app.register_blueprint(items_blueprint)
app.register_blueprint(aad_blueprint)

if __name__ == '__main__':
  app.run(debug=True)