__author__ = 'Zhenyu Yang'


class Category(object):

    def __init__(self, name, get_score_func):
        """
        :param name: str, name of category
        :param get_score_func: function, the calculation function
        """
        self.__name = name
        self.__func = get_score_func

    def getScore(self, array):
        """
        Return the score for the array under the category

        :param array: list, dice numbers
        :return: int, the score
        """
        return self.__func(array)


class DiceOnYacht(object):

    def __init__(self):
        self.__categories = {}

    def addCategory(self, category, get_score_func):
        """
        Register a Category to DiceOnYacht for later using.

        :param category: str, indicating the category name
        :param get_score_func: function, calculate the score for that category
        """
        self.__categories[category] = Category(category, get_score_func)

    def checkValid(self, array):
        if len(array) != 5:
            print 'invalid input array'
            return False
        for n in array:
            if n not in range(1, 9):
                return False
        return True

    def getScore(self, category, array):
        """
        Get score for the array under a category.

        :param category: str, category name
        :param array: list, dice numbers
        :return: int, the score of the array under the category
        """
        if not self.checkValid(array):
            return

        if category in self.__categories:
            return self.__categories[category].getScore(array)
        return 0

    def getSuggestion(self, array):
        """
        Get suggestion category with highest potential score.

        :param array: list, dice numbers
        :return: str, the name of category with highest score
        """
        if not self.checkValid(array):
            return

        suggestion, score = '', 0
        for category in self.__categories:
            s = self.__categories[category].getScore(array)
            if not suggestion or s > score:
                suggestion, score = category, s
        return suggestion


if __name__ == '__main__':
    dice_on_yacht = DiceOnYacht()

    from Categories import categories
    for category in categories:
        dice_on_yacht.addCategory(category, categories[category])

    print dice_on_yacht.getScore('AllSame', [1, 1, 1, 1, 1])
    print dice_on_yacht.getScore('Fours', [4, 4, 4, 4, 5])
    print dice_on_yacht.getScore('SmallStraight', [1, 2, 3, 4, 7])
    print dice_on_yacht.getSuggestion([8, 8, 5, 8, 2])
