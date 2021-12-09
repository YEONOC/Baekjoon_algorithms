n = int(input())
arr = []
num = [1 for _ in range(n)]

for _ in range(n) :
    kg, height = map(int, input().split())
    arr.append([kg, height])

for i in range(n) :
    for j in range(n) :
        if (i == j) :
            continue
        if (arr[i][0] < arr[j][0]) :
            if (arr[i][1] < arr[j][1]) :
                num[i] += 1

for i in range(n) :
    print(num[i], end=' ')