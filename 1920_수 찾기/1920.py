def binarysearch(num, a, l, h) :
    if (l > h) :
        return 0
    mid = (l + h) // 2

    if (num[mid] == a) :
        return 1
    elif num[mid] < a :
        return binarysearch(num, a, mid+1, h)
    else :
        return binarysearch(num, a, l, mid-1)


N, num = int(input()), list(map(int, input().split()))
num.sort()

M, Mum= int(input()), list(map(int, input().split()))
l = 0
h = N - 1
for i in range(M) :
    print(binarysearch(num, Mum[i], l , h))