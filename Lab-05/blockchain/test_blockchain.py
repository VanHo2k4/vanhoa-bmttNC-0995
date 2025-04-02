from blockchain import Blockchain

my_blockchain = Blockchain()

my_blockchain.add_transaction('David', 'Eve', 15)

previous_block = my_blockchain.get_previous_block()
previous_proof = previous_block.proof

new_proof = my_blockchain.proof_of_work(previous_proof)

previous_hash = previous_block.hash
new_block = my_blockchain.create_block(new_proof, previous_hash)

print("Block mới đã được thêm vào blockchain:")
print(new_block.__dict__)

my_blockchain.add_transaction('Eve', 'Frank', 7)
my_blockchain.add_transaction('Frank', 'David', 2)

for block in my_blockchain.chain:
    print(f"Block #{block.index}")
    print("Timestamp:", block.timestamp)
    print("Transactions:", block.transactions)
    print("Proof:", block.proof)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("-------------")

print("Is Blockchain Valid:", my_blockchain.is_chain_valid(my_blockchain.chain))