class BIT:

    def __init__(self, N):
        self.bit = [0] * (1 + N)
        self.num = N

    def update(self, index, value):
        k = index
        while k <= self.num:
            self.bit[k] += value
            k += -k & k

    def query(self, index):
        result = 0
        k = index
        while k > 0:
            result += self.bit[k]
            k -= -k & k
        return result


import sys
inp = sys.stdin
inp = open("input.txt")

n, T = map(int, inp.readline().split())
tree = {i: [] for i in xrange(1, 1 + n)}
root = (1 + n) * n / 2
for i in xrange(1, n):
    e, s = map(int, inp.readline().split())
    root -= s
    tree[e].append(s)


bitree = BIT(n)
bitree.update(root, 1)

# keep (node, child_index) in the stack
stack = [[root, 0]]

similar_pair_num = 0

while stack:

    node, index = stack[-1]
    if index >= len(tree[node]):
        # already traverse all children
        # return to topper layer
        stack.pop()
        # remove the node from BItree
        bitree.update(node, -1)
    else:
        # the next child of current node
        child = tree[node][index]
        # move to next child when comes back
        stack[-1][1] += 1

        similar_pair_num += bitree.query(min(T + child, n)) - bitree.query(max(child - T - 1, 0))

        # go to child node layer
        stack.append([child, 0])

        # add the child node into bitree
        bitree.update(child, 1)

print similar_pair_num





