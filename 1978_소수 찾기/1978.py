import math

n, num = int(input()), list(map(int, input().split()))
pt = 0
max_num = max(num)
prime_list = [i for i in range(max_num+1)]

m = math.floor(max_num ** 0.5)

for i in range(2, m+1) :
    if (i in prime_list) :
        for j in range(i+i, max_num+1, i) :
            if (j in prime_list) :
                prime_list.remove(j)
            else :
                continue

prime_list.remove(0)
prime_list.remove(1)
for i in range(n) :
    if num[i] in prime_list :
        pt += 1
print(pt)