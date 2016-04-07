class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        res = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in reversed(range(1, len(ratings))):
            if ratings[i-1] > ratings[i] and res[i-1]<=res[i]:
                res[i-1] = res[i] + 1
        return sum(res)


