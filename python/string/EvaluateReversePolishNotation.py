class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        ops = ['+', '-', '*', '/']
        i = 0
        res = []
        while i < len(tokens):
            x = tokens[i]
            if x not in ops:
                x = int(x)
                res.append(x)
            else:
                y2 = res.pop()
                y1 = res.pop()*1.0
                if x == '-':
                    res.append(int(y1-y2))
                elif x == '+':
                    res.append(int(y1+y2))
                elif x == '*':
                    res.append(int(y1*y2))
                elif x == '/':
                    res.append(int(y1/y2))
            i += 1
        return res[0]
