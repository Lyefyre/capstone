from data import *

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


class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        number_collisions = 1

        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

    if possible_return_value is None:
        return None

    if possible_return_value[0] == key:
        return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
        new_hash_code = self.hash(key, retrieval_collisions)
        retrieving_array_index = self.compressor(new_hash_code)
        possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return


hash_map = HashMap(15)
hash_map.assign('asian', 'Meng-Fao')
hash_map.assign('german', 'Brezlstube')
hash_map.assign('greek', 'Athens')
print(hash_map.retrieve('asian'))
print(hash_map.retrieve('german'))
print(hash_map.retrieve('greek'))


print("Welcome to the SoHo Restauran!")
print("""What type of food would you like to eat?
Type the beginning of the food to see, if it is available!""")
