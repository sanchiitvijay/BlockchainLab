import hashlib
import time

# Define the Block class
class Block:
    def __init__(self, block_data, block_number, previous_hash=''):
        self.block_number = block_number 
        self.header = f"Block #{self.block_number}" 
        self.previous_hash = previous_hash 
        self.timestamp = time.time()  
        self.nonce = 0 
        self.block_data = block_data 
        self.hash = self.calculate_hash() 
        self.next_block = None 

    def calculate_hash(self):
        try:
            
            block_content = (str(self.block_number) + 
                             str(self.header) + 
                             str(self.previous_hash) + 
                             str(self.timestamp) + 
                             str(self.nonce) + 
                             str(self.block_data))
            return hashlib.sha256(block_content.encode()).hexdigest()
        except Exception as e:
            raise RuntimeError("Error calculating hash") from e

    def mine_block(self, difficulty):
        target = '0' * difficulty  
        while not self.hash.startswith(target):
            self.nonce += 1  
            self.hash = self.calculate_hash() 

    def __str__(self):
        return (f"{self.header}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Nonce: {self.nonce}\n"
                f"Hash: {self.hash}\n"
                f"Block Data: {self.block_data}\n")


class Blockchain:
    def __init__(self, difficulty=2):
        self.head = None 
        self.tail = None 
        self.difficulty = difficulty 
        self.block_number = 0 

    def add_block(self, block_data):
        self.block_number += 1 
        if self.head is None:
            new_block = Block(block_data, self.block_number)
            new_block.mine_block(self.difficulty) 
            self.head = new_block
            self.tail = new_block
        else:
            new_block = Block(block_data, self.block_number, self.tail.hash)
            new_block.mine_block(self.difficulty)
            self.tail.next_block = new_block 
            self.tail = new_block

    def display_chain(self):
        current_block = self.head
        while current_block:
            print(current_block)
            current_block = current_block.next_block


blockchain = Blockchain(difficulty=2)

blockchain.add_block(["Transaction 1: Alice -> Bob: 10 BTC", "Transaction 2: Bob -> Charlie: 5 BTC"])
blockchain.add_block(["Transaction 3: Charlie -> Alice: 2 BTC"])
blockchain.add_block(["Transaction 4: Bob -> Alice: 3 BTC"])

blockchain.display_chain()