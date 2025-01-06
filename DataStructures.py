# Array

class Array:
    """
        Array Constructor.\n
        Defines Array Data Structure.\n
        \n
        Args:\n
        arr list[int] => List of data that should be initally present in the array. Initially empty.\n
        size [int] => Size of the array. if not specifed, it will be the size of arr provided.\n
        \n
        Caution, Use size and/or arr parameter to initalize Array
    """
    def __init__(self, **kwargs:list[int] | int):
        try:
            self.size = kwargs['size'] # size key was given, defined by user

        except KeyError:
            self.size = len(kwargs['arr']) # not defined by user
        
        self.array = [None] * self.size
        self.N = 0
        
        try:
            for i,val in enumerate(kwargs['arr']):
                self.array[i] = val 
                self.N += 1

        except IndexError as e:
            print(e, "\nIndex Error => Insufficient Array Size")
            exit()

    def __add__(self, arr:list[int]=[]):
        arr = list(arr)
        for i in range(len(arr)):
            if self.N == self.size:
                self.array = self.array + [None]*self.size
            
            self.array[self.N] = arr[0]
            self.N += 1
            i += 1

            del arr[0]
            
    def __getitem__(self, val):
        return self.array[val]
    
    def __setitem__(self, index, val):
        self.array[index] = val

    def __str__(self) -> str:
        return str(self.array[:self.N])

    def __delitem__(self, index):
        
        for i in range(index, self.N):
            self.array[i] = self.array[i+1]
        
        self.N -= 1

    def insert(self, val, loc=-1):
        if loc < 0:
            loc = self.N + loc + 1
        
        if self.N == self.size:
            self.array = self.array + [None]*self.size
        
        arr = self.array.copy()

        for i in range(loc+1, self.N+1):
            arr[i] = self.array[i-1]

        self.array = arr
        
        self.array[loc] = val
        self.N += 1

# Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.head:
            return "Empty"
        
        node = self.head
        _str = f'{str(node.data)}'

        while node.next:
            node = node.next
            _str += f' -> {str(node.data)}'
        
        return _str

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        
        else:
            node = self.head
            while node.next:
                node = node.next

            node.next = Node(data)
    
    def __delitem__(self, data):
        node = self.head

        if data == self.head.data:
            self.head = self.head.next
        
        while node.next:
            if data == node.next.data:
                node.next = node.next.next
                break
            node = node.next


class Stack:

    def __init__(self):
        self.stack = LinkedList()
        self.size = 0
    
    def __str__(self):
        _str = ''
        
        node = self.stack.head
        while node:
            _str = f'|{str(node.data)}|' + '\n' + _str
            node = node.next

        return _str

    
    def push(self, val) -> None:
        self.stack.insert(val)
        self.size += 1

    def pop(self) -> object:
        val = self.stack[self.stack.N - 1]
        self.stack[self.stack.N - 1 ] = None
        return val

    def peek(self) -> object:
        node = self.stack.head
        while node.next:
            node = node.next
        
        return node.data
    
    def isEmpty(self) -> bool:
        if self.size < 1:
            return False
        return True

        


if __name__ == '__main__':

    s = LinkedList()
    s.insert(10)
    s.insert(15)
    s.insert(20)
    s.insert(25)
    s.insert(30)

    print(s)
    
    del s[20]

    print(s)
