from flask import Flask, request, jsonify, render_template
import uuid
import time

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def index():
    # Serves the index.html file
    return render_template('index.html')

@app.route('/api/pay/card', methods=['POST'])
def pay_card():
    data = request.json
    
    # 1. Validate fields exist
    required = ['cardNumber', 'cardName', 'cardExpiry', 'cardCvv']
    for field in required:
        if not data.get(field):
            return jsonify({"success": False, "message": f"Missing {field}"}), 400

    # 2. Simulate validation (Luhn algorithm check would go here in production)
    card_num = data['cardNumber'].replace(' ', '')
    if len(card_num) != 16 or not card_num.isdigit():
        return jsonify({"success": False, "message": "Invalid card number"}), 400

    # 3. Simulate processing delay
    time.sleep(2)

    # 4. Generate mock transaction record
    txn_id = f"TXN-{uuid.uuid4().hex[:6].upper()}"
    
    # In a real app, you would integrate Stripe/PayPal/Razorpay SDK here
    return jsonify({
        "success": True,
        "message": "Payment processed successfully",
        "transactionId": txn_id,
        "amount": 249.99,
        "method": "Card"
    }), 200

@app.route('/api/pay/upi', methods=['POST'])
def pay_upi():
    data = request.json
    upi_id = data.get('upiId', '')

    # Simple regex for UPI validation (e.g., name@okhdfcbank)
    if '@' not in upi_id:
        return jsonify({"success": False, "message": "Invalid UPI ID"}), 400
        
    time.sleep(1.5)
    txn_id = f"TXN-{uuid.uuid4().hex[:6].upper()}"

    return jsonify({
        "success": True,
        "message": "UPI Payment successful",
        "transactionId": txn_id,
        "amount": 249.99,
        "method": "UPI"
    }), 200

if __name__ == '__main__':
    # Run on port 5000
    app.run(debug=True, port=5000)
