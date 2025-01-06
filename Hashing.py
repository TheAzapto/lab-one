import hashlib

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return str([self.key, self.value])

class HashTable:
    def __init__(self):
        self.table = [None] * 256
    
    def append(self, Node:Node):
        key = self.hash(Node.key) % 256

        if self.table[key] == None:
            self.table[key] = Node
        else:
            self.table[key].next = Node

    def hash(self, key:str) -> int:
        return int.from_bytes(hashlib.sha256(bytes(key, 'utf-8')).digest())

    def __str__(self):
        for data in self.table:
            if data:
                print(data, end=' ')
                while data.next:
                    data = data.next 
                    print(data, end=' ')
        
        return str()


table = HashTable()
table.append(Node('1', "one"))
table.append(Node('Name', 'Aayush'))
table.append(Node('NaMe', 'Aayush'))

print(table)
