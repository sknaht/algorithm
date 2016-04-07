class TrieNode:
    def __init__(self, ch):
        self.ch = ch
        self.children = {}
        self.isword = False

class TrieTree:
    def __init__(self):
        self.root = TrieNode('')

    def insert(self, word):
        if not word:
            return
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.isword = True

class WordDictionary:

    def __init__(self):
        self.tree = TrieTree()

    def addWord(self, word):
        self.tree.insert(word)

    def search(self, word):

        def find(i, node):
            if i > len(word):
                return node.isword
            if word[i - 1] == '.':
                for c in node.children:
                    if find(i + 1, node.children[c]):
                        return True
            else:
                if word[i - 1] in node.children:
                    return find(i + 1, node.children[word[i - 1]])
            return False

        return find(1, self.tree.root)

t = WordDictionary()
t.addWord('at')
t.addWord('and')
t.addWord('an')
t.addWord('add')
t.addWord('a')
t.addWord('bat')
print t.search('.at')
print t.search('.a')

