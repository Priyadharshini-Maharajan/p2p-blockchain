import requests
from blockchain import Block

def consensus(blockchain, peers):
    longest_chain = None
    max_length = len(blockchain.chain)

    for node in peers:
        try:
            response = requests.get(f"{node}/chain")
            data = response.json()
            length = data['length']
            chain = data['chain']

            if length > max_length:
                max_length = length
                longest_chain = chain
        except:
            continue

    if longest_chain:
        blockchain.chain = [Block(**block) for block in longest_chain]
        return True
    return False
