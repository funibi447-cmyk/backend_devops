from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/save', methods=['POST'])
def save_data():
    text = request.get_data(as_text=True)
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")
    return {"status": "saved"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    