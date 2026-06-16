from flask import Flask, render_template, request, jsonify
from data import USERS, calculate_cipher_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', users=USERS)

@app.route('/send_money', methods=['POST'])
def send_money():
    data = request.json
    sender = data.get('sender_name')
    password = data.get('password')
    receiver = data.get('receiver_name')
    amount = int(data.get('amount', 0))

    if sender not in USERS or USERS[sender]['password'] != password:
        return jsonify({"status": "error", "message": "Invalid Sender Name or Password!"})

    if receiver not in USERS:
        return jsonify({"status": "error", "message": "Receiver Account not found!"})

    if USERS[sender]['balance'] < amount:
        return jsonify({"status": "error", "message": f"Insufficient Balance! You only have Rs. {USERS[sender]['balance']:,}"})

    # Execute auto-transfer in data.py state
    USERS[sender]['balance'] -= amount
    USERS[receiver]['balance'] += amount

    return jsonify({"status": "success", "message": f"Successfully transferred Rs. {amount:,} to {receiver}!"})

@app.route('/sell_domain', methods=['POST'])
def sell_domain():
    data = request.json
    username = data.get('username')
    domain = data.get('domain')
    password = data.get('password')
    target_account = data.get('target_account')

    # Generate expected cipher password
    expected_password = calculate_cipher_password(username, domain)

    if password != expected_password:
        return jsonify({"status": "error", "message": f"Invalid Cipher Password! Expected format: {expected_password}"})

    if target_account not in USERS:
        return jsonify({"status": "error", "message": "Target reward account does not exist!"})

    # Process rewards: +10,000 Rs & +1 Star
    USERS[target_account]['balance'] += 10000
    USERS[target_account]['stars'] += 1

    # Level Up Logic: Every 5 stars increases level by 1
    new_level = 1 + (USERS[target_account]['stars'] // 5)
    USERS[target_account]['level'] = new_level

    return jsonify({
        "status": "success", 
        "message": f"Domain Sold! Rs. 10,000 added to {target_account}. Total Stars: {USERS[target_account]['stars']} (Level: {USERS[target_account]['level']})"
    })

if __name__ == '__main__':
    app.run(debug=True)
