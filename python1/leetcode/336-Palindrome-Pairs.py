class TrieNode:

    def __init__(self):
        self.nextchar = {}
        self.position = 0
        for i in xrange(26):
            c = chr(ord('a') + i)
            self.nextchar[c] = None


class TrieTree:

    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word, position):

        node = self.root

        for c in word:
            if not node.nextchar[c]:
                node.nextchar[c] = TrieNode()

            node = node.nextchar[c]

        node.position = position

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        trie = TrieTree()
        for i, w in enumerate(words):
            trie.add_word(w, i)



if __name__ == "__main__":
    trie = TrieTree()
    trie.add_word("abc", 11)
    print "over"



