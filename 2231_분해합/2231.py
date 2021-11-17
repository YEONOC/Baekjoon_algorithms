n = int(input())

for i in range(1, n+1) :
    mm = i
    answer = 0
    num = list([0,0,0,0,0,0,0])
    for j in range(len(num)) :
        num[6 - j] = (mm % 10)
        mm = mm // 10
    print(num)
    for j in range(len(num)) :
        answer += num[j]
    answer += i
    if (answer == n) :
        print(i)
        break
    elif (i == n) :
        print(0)