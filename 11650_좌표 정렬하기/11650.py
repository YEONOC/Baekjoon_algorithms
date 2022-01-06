n = int(input())
num = []

for i in range(n) :
    x, y = map(int, input().split())
    num.append([x, y])

num.sort(key=lambda x:(x[0], x[1]))

for _ in num :
    print(_[0], _[1])