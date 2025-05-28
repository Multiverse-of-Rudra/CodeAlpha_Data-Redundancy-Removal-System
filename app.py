from flask import Flask, request, jsonify, render_template
from redundancy_checker import get_hash, is_redundant
import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.form.get('data')
    data_hash = get_hash(data)
    existing_hashes = db.fetch_existing_hashes()

    if is_redundant(data, existing_hashes):
        return jsonify({"status": "fail", "message": "Redundant data"})
    else:
        db.insert_data(data, data_hash)
        return jsonify({"status": "success", "message": "Data added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
