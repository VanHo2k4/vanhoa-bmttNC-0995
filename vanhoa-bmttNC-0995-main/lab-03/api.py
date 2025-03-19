from flask import Flask, request, jsonify
from cipher.rsa import RSACipher

app = Flask(__name__)
rsa_cipher = RSACipher()

@app.route('/api/rsa/generate_key', methods=['GET'])
def rsa_generate_key():
    rsa_cipher.generate_key()
    return jsonify({'message': 'Key generated successfully'})

@app.route('/api/rsa/encrypt', methods=['POST'])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
        encrypted_text = rsa_cipher.encrypt_text(message, private_key)
    