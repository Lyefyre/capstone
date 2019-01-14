class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        isWord = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                isWord = False
                break

    if not isWord:
        while i < len(word):
            current_node.addChild(word[i])
            current_node = current_node.children[word[i]]
            i += 1

    current_node.word = word

    def find_words(self, prefix):
        words = []

        top_node = self.root

        for char in prefix:
            if char in top_node.children:
                top_node = top_node.children[char]
            else:
                return words

        if top_node == self.root:
            queue = [node for key, node in top_node.children.items()]
        else:
            queue = [top_node]

        while queue:
            current_node = queue.pop()
            if current_node.word is not None:
                words.append(current_node.word)

        queue = [node for key, node in current_node.children.items()] + queue

        return words


class TrieNode:
    def __init__(self, key=None, word=None):
        self.key = key
        self.word = word
        self.children = {}

    def addChild(self, char, value=None):
        self.children[char] = TrieNode(char, value)