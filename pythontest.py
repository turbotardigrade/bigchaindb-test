from bigchaindb import Bigchain
b = Bigchain()

from bigchaindb import crypto
import time

# Create a test user
testuser1_priv, testuser1_pub = crypto.generate_key_pair()
admin_priv, admin_pub = crypto.generate_key_pair()

# Define a digital asset data payload
digital_asset_payload = {'msg': 'Hello BigchainDB!'}

# A create transaction uses the operation `CREATE` and has no inputs
tx = b.create_transaction(b.me, [admin_pub, testuser1_pub], None, 'CREATE', payload=digital_asset_payload)

# All transactions need to be signed by the user creating the transaction
tx_signed = b.sign_transaction(tx, b.me_private)

# Write the transaction to the bigchain.
# The transaction will be stored in a backlog where it will be validated,
# included in a block, and written to the bigchain 
b.write_transaction(tx_signed)

time.sleep(2)

tid = tx_signed["id"]
print(tid)
# Retrieve a transaction from the bigchain
tx_retrieved = b.get_transaction(tid)
print()
print(tx_retrieved)
print()
print(tx_retrieved["transaction"]["data"]["payload"])

