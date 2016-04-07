__author__ = 'Zhenyu Yang'


def getScoreForOneKind(num):
    """
    :param num:
    :return: function for calculating score
    """
    def getScore(array):
        count = 0
        for n in array:
            if n == num:
                count += num
        return count

    return getScore


def getScoreXOfAKind(x):

    def getScore(array):
        nums = {i: 0 for i in xrange(1, 9)}
        for n in array:
            nums[n] += 1
            if nums[n] >= x:
                return sum(array)
        return 0

    return getScore


def getScoreStraight(length, score):

    def getScore(array):
        sa = sorted(array)
        prev, count = 0, 0
        for n in sa:
            if n - prev == 1:
                prev, count = n, count + 1
                if count == length:
                    return score
            else:
                prev, count = n, 1
        return 0

    return getScore


def getScoreFullHouse(array):

    s = set(array)
    if len(s) != 2:
        return 0
    c = 0
    for n in array:
        if n == array[0]:
            c += 1
    return 25 if c == 2 or c == 3 else 0


def getScoreForDistinct(target, score):

    def getScore(array):
        return score if len(set(array)) == target else 0
    return getScore


def getScoreChance(array):
    return sum(array)


categories = dict(
    Ones=getScoreForOneKind(1),
    Twos=getScoreForOneKind(2),
    Threes=getScoreForOneKind(3),
    Fours=getScoreForOneKind(4),
    Fives=getScoreForOneKind(5),
    Sixes=getScoreForOneKind(6),
    Sevens=getScoreForOneKind(7),
    Eights=getScoreForOneKind(8),
    ThreeOfAKind=getScoreXOfAKind(3),
    FourOfAKind=getScoreXOfAKind(4),
    FullHouse=getScoreFullHouse,
    SmallStraight=getScoreStraight(4, 30),
    LargeStraight=getScoreStraight(5, 40),
    AllDifferent=getScoreForDistinct(5, 40),
    AllSame=getScoreForDistinct(1, 50),
    Chance=getScoreChance
)

