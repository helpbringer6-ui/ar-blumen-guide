from flask import Flask, jsonify
from flower_database import FlowerDatabase

app = Flask(__name__)
database = FlowerDatabase()

@app.route('/flower/<name>')
def get_flower(name):
    info = database.get_flower_info(name)
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)