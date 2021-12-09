def facto(x) :
    a = 1
    i = x
    while i != 0 :
        a *= i
        i -= 1
    return a


n, k = map(int, input().split())

answer = 0

answer = facto(n) / (facto(k) * facto(n - k))

print(round(answer))