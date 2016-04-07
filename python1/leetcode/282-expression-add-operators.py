"""
 Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:

"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []


Solution:
    DFS
"""


class Solution(object):

    def addOperators(self, num, target):

        if not num:
            return []

        def solve(total, index, last, s):
            if index == len(num):
                if total + last == target:
                    answer.append(s)
            else:
                # if num[index] == '0', the current number should be 0, and no more successive number
                to = index + 1 if num[index] == '0' else len(num)
                for pos in xrange(index, to):
                    curr = int(num[index: pos + 1])
                    solve(total + last, pos + 1, curr, s + '+' + str(curr))
                    solve(total + last, pos + 1, -curr, s + '-' + str(curr))
                    solve(total, pos + 1, last * curr, s + '*' + str(curr))

        answer = []
        end = 1 if num[0] == '0' else len(num)
        for i in xrange(end):
            solve(0, i + 1, int(num[:i + 1]), num[:i + 1])
        return answer

print Solution().addOperators("1000000009", 9)
