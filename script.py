from data import *
from trie import Trie


class Node():
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList():
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.next_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        merker = self.get_head_node()
        while merker:
            if merker.get_value() is not None:
                string_list += str(merker.get_value()) + "\n"
            merker = merker.get_next_node()
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


print("                *               ")
print("  *             *            *  ")
print("  *             *            *  ")
print("  *             *            *  ")
print(" ***           ***          *** ")
print("*****         *****        *****")
print("********************************")
print("********************************")
print("********************************")
print("********************************")
print("________________________________")
print("*                              *")
print("*                              *")
print("* Welcome to SoHo Restaurants! *")
print("*                              *")
print("*______________________________*")

trie = Trie()
for food_type in types:
    trie.insert(food_type)

hashmap = HashMap(len(types))
for food_type in types:
    linkedlist = LinkedList()
    for restaurant in restaurant_data:
        if food_type == restaurant[0]:
            linkedlist.insert_beginning(restaurant)
            hashmap.assign(food_type, linkedlist)

while True:
    user_input = str(input("\nSearch for a food type here. \nType 'quit' anytime to exit.\n")).lower()
    if user_input == 'quit':
        print("Thanks for using SoHo Restaurants.")
        exit()
    user_input_select = str(input("\nYou've picked: {}\nProceed? \n'y' for yes\n'n' for no.\nType 'quit' anytime to exit.\n".format(trie.find_words(user_input)[0]))).lower()
    if user_input_select == 'y':
        ll = hashmap.retrieve(trie.find_words(user_input)[0])
        head_node = ll.get_head_node()
        while head_node.value is not None:
            print("\n")
            print("Name: {}".format(head_node.value[1]))
            print("----------------------")
            print("Type: {}".format(head_node.value[0]))
            print("Price: {}/5".format(head_node.value[2]))
            print("Rating: {}/5".format(head_node.value[3]))
            print("Address: {}".format(head_node.value[4]))
            print("\n")
            head_node = head_node.get_next_node()
    elif user_input_select == 'quit':
        print("Thanks for using SoHo Restaurants.")
        exit()
