# 🚀 P2P Blockchain Network Simulation

This project simulates a peer-to-peer (P2P) blockchain network using **Python**, **Flask**, and a simple web interface.

---

## 📚 Assignment Objective

Simulate a basic blockchain environment to help students understand core concepts like blocks, mining, transactions, Proof of Work (PoW), consensus, and peer node communication.

---

## ✅ Technologies Used

- Python 3.x  
- Flask  
- Requests (for HTTP between nodes)  
- Bootstrap 5 (for web UI)

---

## ✅ Features

### ✅ Simple Blockchain Structure

- Blocks contain:
  - Index
  - Timestamp
  - Transactions
  - Nonce
  - Previous hash
- Transactions include sender, recipient, and amount

### ✅ Proof-of-Work Mining

- Each mined block must satisfy a simple hash puzzle (e.g., leading zeros)
- New transactions are bundled into a block only after mining

### ✅ Multiple Nodes

- Each node runs on a different port
- Maintains its own local copy of the blockchain

### ✅ Node Registration & Discovery

- Nodes can register peers dynamically
- Enables network growth

### ✅ Consensus Algorithm

- Ensures consistency across the network
- Follows "Longest valid chain wins" rule

### ✅ Blockchain Sync

- Any node can request sync to align its chain with peers

### ✅ Professional Web UI

- Add transactions via form
- Trigger mining
- Register peers
- Sync chain
- View blockchain in card layout

---

## ▶️ How to Run This Project

### 1. Install Dependencies

```bash
pip install -r requirements.txt

### 2. Run a Node
Start your first node on port 5000:

```bash
python run_node.py 5000

Start more nodes on different ports:

```bash

python run_node.py 5001
python run_node.py 5002


### 🌐 Open in Browser
Node 1: http://127.0.0.1:5000

Node 2: http://127.0.0.1:5001

Node 3: http://127.0.0.1:5002


