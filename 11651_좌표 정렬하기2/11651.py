n = int(input())
num = list()

for _ in range(n) :
    x, y = map(int, input().split())
    num.append([x, y])

num.sort(key=lambda x:(x[1], x[0]))

for i in num :
    print(i[0], i[1])