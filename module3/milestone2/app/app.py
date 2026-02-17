from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if 'features' not in data:
            return jsonify({"error": "Missing 'features' in request"}), 400

        # Mock inference logic
        prediction = sum(data['features']) / len(data['features'])
        return jsonify({"prediction": prediction, "status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)