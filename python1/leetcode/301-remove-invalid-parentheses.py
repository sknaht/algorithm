class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        curr = [s]
        answer = []

        while not answer:
            next = set([])
            for s in curr:
                left, right = 0, 0
                valid = True
                for i in xrange(len(s)):
                    c = s[i]
                    if c == '(':
                        left += 1
                        next.add(s[:i] + s[i + 1:])
                    if c == ')':
                        right += 1
                        next.add(s[:i] + s[i + 1:])
                    if left < right:
                        valid = False
                if valid and left == right:
                    answer.append(s)
            curr = next

        return answer


    def removeMinInvalidPar(self, s):
        '''
        03/18/2016. Facebook interview question, from baiqi.
                    given a string of "(" and ")"
                    remove the minimum number of parentheses to make it valid
        :param s:
        :return:
        '''


        '''
        using a stack to store valid strings, like below

        (, (), (, (()()), (, (

        the single ( is invalid (
        '''
        stack = []

        invalid_left, invalid_right = 0, 0

        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if stack:
                    if stack[-1] == '(':
                        # merge with the last (
                        stack[-1] = '()'
                    else:
                        # the previous one is (
                        if len(stack) > 1:
                            stack[-1] = '(' + stack.pop() + ')'
                        else:
                            invalid_right += 1

                    while len(stack) > 1 and stack[-2] != '(':
                        t = stack.pop()
                        stack[-1] += t
                else:
                    invalid_right += 1

            else:
                continue

        r = ""
        for t in stack:
            if t != '(':
                r += t
            else:
                invalid_left += 1

        #-----------------------

        # using dfs to search all possible valid string

        def dfs(s, i, current, result, left, right, invalid_left, invalid_right):

            if i >= len(s):
                if left == right:
                    result.add(current)
                return

            if s[i] == '(':
                # remove this (
                if invalid_left:
                    dfs(s, i + 1, current, result, left, right, invalid_left - 1, invalid_right)
                # keep this (
                dfs(s, i + 1, current + '(', result, left + 1, right, invalid_left, invalid_right)
            elif s[i] == ')':
                # remove this )
                if invalid_right:
                    dfs(s, i + 1, current, result, left, right, invalid_left, invalid_right - 1)

                # keep this ) with condition
                if right < left:
                    dfs(s, i + 1, current + ')', result, left, right + 1, invalid_left, invalid_right)
            else:
                dfs(s, i + 1, current + s[i], result, left, right, invalid_left, invalid_right)

        result = set([])
        dfs(s, 0, "", result, 0, 0, invalid_left, invalid_right)
        if not result:
            result = [""]
        return list(result)




print Solution().removeMinInvalidPar( ")(f")
