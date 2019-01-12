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


print("Welcome to the SoHo Restauran!")
print("""What type of food would you like to eat?
Type the beginning of the food to see, if it is available!""")
