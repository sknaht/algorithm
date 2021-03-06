"""
tag: dp, bitmasks

http://codeforces.com/problemset/problem/8/C

solution:
for one already optimized selection a: 0101100101
calculate each 0 positions, e.g. 0101100111, meaning selecting the second
item based on the a status.
then select another one item, e.g. 0101101111, meaning selecting the
fourth item based on the a status.
and we need another array to keep the path from a to b
the solution is what kept in status a=1111111111

got TLE for n=24
"""


import sys

ip = sys.stdin.readline
ip = open('../input.txt').readline

# reading numbers of one line
def getnums():
    return map(int, ip().split())

# distance
def f(x, y):
    return x * x + y * y


# the original point
xo, yo = getnums()

# number of items
n = int(ip())

# distance from original point to each item
disto = [0] * n

# distance from each item to another item
disti = [[0] * n for i in xrange(n)]

# position of items
positions = []

pow = [2 ** i for i in xrange(n)]

# calculate distance between 2 items
for i in xrange(n):
    x, y = getnums()
    disto[i] = f(xo - x, yo - y)
    for j in xrange(i):
        disti[j][i] = f(positions[j][0] - x, positions[j][1] - y)
        disti[i][j] = disti[j][i]
    positions.append((x, y))


# optimized cost for each status
a = [None] * (1 << n)
# none of the items are selected, so the cost is 0
a[0] = 0
# parent status for each optimized status
p = [0] * (1 << n)

for i in xrange(1 << n):
    if a[i] is not None:
        for j in xrange(n):
            # meaning jth items was not selected in status i
            if i & pow[j] == 0:

                # only take the item and return
                t = i + pow[j]
                if not a[t] or a[t] > a[i] + disto[j] * 2:
                    a[t] = a[i] + disto[j] * 2
                    p[t] = i

                # if take another item
                for k in xrange(j + 1, n):
                    if t & pow[k] == 0:
                        two = t + pow[k]
                        c = a[i] + disto[j] + disti[j][k] + disto[k]
                        if not a[two] or a[two] > c:
                            a[two] = c
                            p[two] = i

                # still have no idea about the break...
                break

z = (1 << n) - 1
print a[z]
r = [0]
while z > 0:
    t = z - p[z]
    while t:
        x = -t & t
        t -= x
        i = 0
        while x > 0:
            i += 1
            x /= 2
        r.append(i)
    z = p[z]
    r.append(0)

print ' '.join(map(str, r))






