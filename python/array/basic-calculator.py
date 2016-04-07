class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):

        s = s.replace(" ", '')
        nums, opts = [], []

        priority = {
            '/': 4,
            '*': 4,
            '+': 3,
            '-': 3,
            ')': 2,
            '(': 5
        }

        def cal(n2, n1, o):
            if o == '+':
                return n1 + n2
            if o == '-':
                return n1 - n2
            if o == '*':
                return n1 * n2
            if o == '/':
                return n1 / n2

        i = 0
        while i < len(s):
            if s[i] in priority:
                while opts and opts[-1] != '(' and priority[opts[-1]] >= priority[s[i]]:
                    nums.append(cal(nums.pop(), nums.pop(), opts.pop()))
                if s[i] == ')':
                    opts.pop()
                else:
                    opts.append(s[i])
                i += 1
            else:
                t = 0
                while i < len(s) and s[i] in '0123456789':
                    t = t * 10 + ord(s[i]) - ord('0')
                    i += 1
                nums.append(t)

        while opts:
            nums.append(cal(nums.pop(), nums.pop(), opts.pop()))

        return nums[-1]

print Solution().calculate('3+10 / (4+1)')

