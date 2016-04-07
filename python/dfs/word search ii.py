class TrieNode:

    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:

    def __init__(self, root):
        self.root = root

    def insert(self, word):
        word = word.strip()
        if not word:
            return
        t = self.root
        for c in word:
            if c in t.children:
                t = t.children[c]
            else:
                t.children[c] = TrieNode()
                t = t.children[c]
        t.count += 1


class Solution:
    # @param {character[][]} board
    # @param {string[]} words
    # @return {string[]}
    def findWords(self, board, words):
        if not board or (not words):
            return []

        trie = Trie(TrieNode())
        for word in words:
            trie.insert(word)


        def check(ch, node, i, j, curr):
            if not node or (ch not in node.children):
                return
            if node.children[ch].count and curr not in result:
                result.append(curr)

            for (x, y) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ii, jj = x + i , y + j
                if 0 <= ii < len(board) and 0 <= jj < len(board[0]) and not mark[ii][jj]:
                    mark[ii][jj] = True
                    check(board[ii][jj], node.children[ch], ii, jj, curr + board[ii][jj])
                    mark[ii][jj] = False

        result = []
        mark = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                mark[i][j] = True
                check(board[i][j], trie.root, i, j, board[i][j])
                mark[i][j] = False

        return result



print Solution().findWords([
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
], ["oath","pea","eat","rain"])
