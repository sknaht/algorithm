class NestedIterator(object):

    def __init__(self, lst):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack, self.index = [lst], [0]
        self.stored_next = None


    def next(self):
        """
        :rtype: int
        """
        if self.stored_next != None:
            x = self.stored_next
            self.stored_next = None
            return x

        while self.stack:

            # check if the current index exceeds the
            # number of elements in this layer
            if self.index[-1] >= len(self.stack[-1]):
                self.stack.pop()
                self.index.pop()
                continue

            current = self.stack[-1][self.index[-1]]
            self.index[-1] += 1

            if current.isInteger():
                # return the current number
                return current.getInteger()
            else:
                # push into stack
                self.stack.append(current.getList())
                self.index.append(0)

        return None


    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stored_next:
            self.stored_next = self.next()
            return self.stored_next != None

        return True



