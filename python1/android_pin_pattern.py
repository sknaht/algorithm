'''
https://www.zhihu.com/question/24905007/answer/29414497
'''
from itertools import chain, permutations

impossible = {'13': '2', 
              '46': '5', 
              '79': '8', 
              '17': '4', 
              '28': '5', 
              '39': '6', 
              '19': '5', 
              '37': '5',
              '31': '2',
              '64': '5',
              '97': '8',
              '71': '4',
              '82': '5',
              '93': '6',
              '91': '5',
              '73': '5'}

def counts():
    iterlst = chain(*(permutations('123456789', i) for i in range(4, 10)))
    count = 0
    for i in iterlst:
        stri = ''.join(i)
        for k, v in impossible.items():
            if k in stri and v not in stri[:stri.find(k)]:
                break
        else:
            count += 1
    return count

#--------------------------------------------

cross = {
    (1, 3): 2,
    (3, 1): 2,
    (1, 7): 4,
    (7, 1): 4,
    (3, 9): 6,
    (9, 3): 6,
    (7, 9): 8,
    (9, 7): 8,
    (1, 9): 5,
    (2, 8): 5,
    (3, 7): 5,
    (4, 6): 5,
    (6, 4): 5,
    (7, 3): 5,
    (8, 2): 5,
    (9, 1): 5,
}


def count1():

    a = [False] * 10


    def dfs(visited, depth, last):
        count = 0
        if depth >= 4:
            count = 1
        for i in xrange(1, 10):
            if not visited[i] and ((last, i) not in cross or visited[cross[(last, i)]]):
                visited[i] = True
                count += dfs(visited, depth + 1, i)
                visited[i] = False
        return count

    # 1, 3, 7, 9
    a[1] = True
    result = dfs(a, 1, 1) * 4
    a[1] = False

    # 2, 4, 6, 8
    a[2] = True
    result += dfs(a, 1, 2) * 4
    a[2] = False

    # 5
    a[5] = True
    result += dfs(a, 1, 5)
    a[5] = False

    return result



print(count1())#389112

