from flask import Flask, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.txt"

@app.route('/api/save', methods=['POST'])
def save_data():
    text = request.get_data(as_text=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return {"status": "saved"}

@app.route('/api/load', methods=['GET'])
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        return {"data": content}
    return {"data": ""}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)