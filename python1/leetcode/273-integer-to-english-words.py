class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0: return 'Zero'

        numbers = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
            90: 'Ninety', 100: 'Hundred'
        }

        scale = {
            1: 'Thousand',
            2: 'Million',
            3: 'Billion'
        }

        def transform(n):
            s = ''
            if n >= 100:
                s = numbers[n / 100] + ' ' + numbers[100]
            n %= 100
            if n == 0:
                return s

            if n <= 20:
                tail = numbers[n]
            else:
                tail = numbers[n / 10 * 10]
                if n % 10 != 0:
                    tail += ' ' + numbers[n % 10]
            if s:
                return s + ' ' + tail
            else:
                return tail

        answer = transform(num % 1000)
        num /= 1000
        sc = 1
        while num > 0:
            a = transform(num % 1000)
            if a:
                if answer:
                    answer = a + ' ' + scale[sc] + ' ' + answer
                else:
                    answer = a + ' ' + scale[sc]
            num /= 1000
            sc += 1
        return answer


print Solution().numberToWords(1000000)
