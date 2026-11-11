from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/purchase", methods=["POST"])
def create_purchase():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    required_fields = [
        "product_id",
        "description",
        "customer_name",
        "customer_email",
        "price",
        "is_online",
    ]

    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    if not isinstance(data["is_online"], bool):
        return jsonify({"error": "Invalid purchase type"}), 400

    try:
        price = float(data["price"])
    except (ValueError, TypeError):
        return jsonify({"error": "Price must be a number"}), 400

    if not 0 <= price <= 1000:
        return jsonify({"error": "Price must be between $0 and $1,000"}), 400

    return (
        jsonify({"message": "Purchase received successfully!", "purchase": data}),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
