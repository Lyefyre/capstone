##from data import *

class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def getValue(self):
        return self.value

    def getNextNode(self):
        return self.next_node

    def setNextNode(self, next_node):
        self.next_node = next_node


class LinkedList():
    def __init__(self, value=None):
        self.head_node = Node(value)

    def getHeadNode(self):
        return self.head_node

    def insertBeginning(self, new_value):
        new_node = Node(new_value)
        new_node.setNextNode(self.next_node)
        self.head_node = new_node

    def stringifyList(self):
        string_list = ""
        merker = self.getHeadNode()
        while merker:
            if merker.getValue() is not None:
                string_list += str(merker.getValue()) + "\n"
            merker = merker.getNextNode()
        return string_list


class HashMap():
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for array in range(self.array_size)]
    
    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code
        
    def compressor(self, hash_code):
        return hash_code % self.array_size
        
    def assign(self, key, value):
        self.value = self.compressor(self.hash(key))
        self.array = value
    
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]
    
    
print("Welcome to the SoHo Restauran!")
print("""What type of food would you like to eat?
Type the beginning of the food to see, if it is available!""")

hash_map = HashMap(20)
hash_map.assign('asian', 'Meng-Fao')
print(hash_map.retrieve('asian'))

