######################################################################
### BigchainDB
from bigchaindb import Bigchain, crypto
b = Bigchain()

def createTx(payload):
    tx = b.create_transaction(b.me, [admin_pub, testuser1_pub], None, 'CREATE', payload=payload)



######################################################################
### API Server

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/receipts', methods=['POST'])
def add_receipt():
    content = request.json
    print(content)
    return jsonify(content)

@app.route('/receipts/<uuid>', methods=['GET'])
def add_message(uuid):
    return jsonify({"uuid":uuid})

if __name__ == "__main__":
    app.debug = True
    app.run()
