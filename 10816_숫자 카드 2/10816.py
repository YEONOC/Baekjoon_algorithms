import sys
input = sys.stdin.readline

n = int(input())
nn = list(map(int, input().split()))
d = dict()

for i in range(n) :
    try :
        d[nn[i]] += 1
    except KeyError :
        d[nn[i]] = 1
m = int(input())
mn = list(map(int, input().split()))

for i in range(m) :
    try :
        print(d[mn[i]], end=' ')
    except KeyError :
        print(0, end=' ')