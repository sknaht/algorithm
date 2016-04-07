    class Solution:
        # @param {string} input
        # @return {integer[]}
        def diffWaysToCompute(self, input):

            input = input.replace(' ', '')

            nums, opt, i = [], [], 0

            while i < len(input):
                if input[i] in '-+*':
                    opt.append(input[i])
                    i += 1
                else:
                    t = 0
                    while i < len(input) and input[i] in '1234567890':
                        t = t * 10 + ord(input[i]) - ord('0')
                        i += 1
                    nums.append(t)

            def cal(o, n1, n2):
                if o == '+':
                    return n1 + n2
                if o == '-':
                    return n1 - n2
                if o == '*':
                    return n1 * n2

            def make(ns, os):
                if len(ns) == 1:
                    return ns

                tmp = []
                for i in xrange(len(os)):
                    left = make(ns[:i + 1], os[:i])
                    right = make(ns[i + 1:], os[i + 1:])
                    o = os[i]
                    for nl in left:
                        for nr in right:
                            tmp.append(cal(o, nl, nr))
                return tmp

            return make(nums, opt)


    print Solution().diffWaysToCompute("2*3-4*5")
