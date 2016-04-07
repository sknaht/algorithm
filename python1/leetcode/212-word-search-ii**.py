class TreeNode(object):
    def __init__(self):
        self.children = {}
        self.word = ''


class TrieTree(object):
    def __init__(self):
        self.root = TreeNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
        node.word = word

    def check_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
        return node.word


class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board:
            return []

        tree = TrieTree()
        for w in words:
            tree.add_word(w)

        result = set([])
        visited = [ [False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                visited[i][j] = True
                self.search(result, board, visited, i, j, tree.root)
                visited[i][j] = False
        return list(result)

    def search(self, result, board, visited, i, j, node):
        if board[i][j] not in node.children:
            return
        node = node.children[board[i][j]]
        if node.word:
            result.add(node.word)
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x, y = dx + i, dy + j
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y]:
                visited[x][y] = True
                self.search(result, board, visited, x, y, node)
                visited[x][y] = False


print Solution().findWords([['a']], ['a'])