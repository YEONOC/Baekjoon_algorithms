def gcd(a, b) :
    if (a % b == 0) :
        return b
    else :
        return gcd(b, a % b)

x, y = map(int, input().split())
g = 0
if (x >= y) :
    g = gcd(x, y)
else :
    g = gcd(y, x)

l = (x * y) / g

print(g)
print(round(l))