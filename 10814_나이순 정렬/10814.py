n = int(input())

mem = list()

for i in range(n) :
    age, name = map(str, input().split())
    mem.append([int(age), name])

mem.sort(key=lambda x:x[0])

for i in mem :
    print(i[0], i[1])