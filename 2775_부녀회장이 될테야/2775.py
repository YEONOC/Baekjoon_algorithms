t = int(input())

result = 0

for i in range(t) :
    k = int(input())
    n = int(input())
    vila_0 = list([1, 2, 3, 4, 5, 6 ,7, 8 ,9 ,10, 11, 12, 13, 14])
    for j in range(k) :
        vila_k = list()
        nn = 0
        for m in range(14) :
            nn += vila_0[m]
            vila_k.append(nn)
        vila_0 = vila_k
    result = vila_k[n-1]   


    print(result)