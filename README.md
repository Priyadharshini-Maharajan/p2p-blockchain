🚀 P2P Blockchain Network Simulation
This project simulates a peer-to-peer (P2P) blockchain network using Python, Flask, and a simple web interface. It demonstrates the core building blocks of blockchain technology including mining, Proof of Work, transactions, peer syncing, and consensus.

📚 Assignment Objective
Simulate a basic blockchain environment to help students understand core concepts like:

Blocks and transactions
Mining and Proof of Work (PoW)
Node registration and discovery
Consensus mechanism
Peer-to-peer communication
✅ Technologies Used
Python 3.x
Flask – Web framework
Requests – HTTP requests for peer-to-peer communication
Bootstrap 5 – Responsive UI styling
✅ Features
✅ Simple Blockchain Structure
Each block includes:

Index
Timestamp
List of transactions
Nonce
Previous hash
Transactions contain:

Sender
Recipient
Amount
✅ Proof-of-Work Mining
Blocks are mined using a hash puzzle (e.g., leading zeros).
New transactions are bundled into a block only after successful mining.
✅ Multi-node Simulation
Each node runs independently on a different port.
Nodes maintain their own local copy of the blockchain.
✅ Node Registration & Discovery
Nodes can register new peers dynamically.
Promotes network expansion and decentralization.
✅ Consensus Algorithm
Ensures consistency across the network.
"Longest valid chain wins" rule applied.
✅ Blockchain Synchronization
Nodes can sync with others to fetch the most updated valid chain.
✅ Professional Web UI
Add new transactions
Trigger mining
Register peers
Sync the chain
View blockchain blocks in a user-friendly card layout
▶️ How to Run This Project
1. Install Dependencies and Start the Nodes
pip install -r requirements.txt
Start your first node on port 5000

python run_node.py 5000
Start additional nodes on different ports (in separate terminals)

python run_node.py 5001
python run_node.py 5002
2. Open in Browser
Node 1: http://127.0.0.1:5000
Node 2: http://127.0.0.1:5001
Node 3: http://127.0.0.1:5002
🧭 How to Use
➕ Add Transaction Fill in:

Author

Content

Click "Add Transaction"

🔨 Mine a Block Click "Mine Block"

Block will be created and added to the chain

🔗 Register Nodes Enter peer addresses (e.g., http://127.0.0.1:5001)

Click "Register Peers"

👀 View Blockchain Blocks are displayed as cards in the UI