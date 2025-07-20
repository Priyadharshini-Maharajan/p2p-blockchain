from flask import Flask, request, jsonify, render_template, redirect, url_for
from blockchain import Blockchain
import requests

app = Flask(__name__)
blockchain = Blockchain()

# ✅ Home
@app.route('/')
def index():
    return render_template('index.html', peers=list(blockchain.peers))

# ✅ View full blockchain
@app.route('/chain')
def view_chain():
    chain_data = [block.to_dict() for block in blockchain.chain]
    return render_template('chain.html', chain=chain_data)

# ✅ Mine a new block
@app.route('/mine')
def mine_block():
    block = blockchain.mine()
    if not block:
        return render_template('mine.html', block=None, message="No transactions to mine.")
    return render_template('mine.html', block=block.to_dict(), message="Block successfully mined!")

# ✅ Add a transaction (GET = form, POST = submit)
@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        tx_data = request.form
        required_fields = ['author', 'content']
        if not all(field in tx_data for field in required_fields):
            return "Missing fields", 400
        blockchain.add_new_transaction({
            "author": tx_data["author"],
            "content": tx_data["content"]
        })
        return redirect(url_for('view_pending_tx'))
    return render_template('add_transaction.html')

# ✅ View pending transactions
@app.route('/pending_tx')
def view_pending_tx():
    return render_template('pending_tx.html', transactions=blockchain.unconfirmed_transactions)

# ✅ Register with another peer
@app.route('/register_with', methods=['GET', 'POST'])
def register_with():
    if request.method == 'POST':
        node_address = request.form.get("node_address")
        if not node_address:
            return "Invalid data", 400

        # Send a request to register with the node
        try:
            response = requests.post(f"{node_address}/register_node", json={
                "node_address": request.host_url
            })

            if response.status_code == 200:
                blockchain.peers.add(node_address)
                return redirect(url_for('index'))
            else:
                return "Failed to register", 400

        except requests.exceptions.ConnectionError:
            return "Connection error. Make sure the peer node is running.", 500

    return render_template('register_with.html')

# ✅ Accept registration from other nodes
@app.route('/register_node', methods=['POST'])
def register_node():
    data = request.get_json()
    node_address = data.get("node_address")
    if not node_address:
        return "Invalid data", 400

    blockchain.peers.add(node_address)
    return jsonify({"message": "Node registered successfully."}), 200

# ✅ Get all peers
@app.route('/peers')
def get_peers():
    return jsonify({"peers": list(blockchain.peers)})

if __name__ == '__main__':
    import sys
    port = 5000 if len(sys.argv) < 2 else int(sys.argv[1])
    app.run(host='127.0.0.1', port=port, debug=True)
