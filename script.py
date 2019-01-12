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


print("Welcome to the SoHo Restauran!")
print("""What type of food would you like to eat?
Type the beginning of the food to see, if it is available!""")