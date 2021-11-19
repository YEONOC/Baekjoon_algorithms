n, m = map(int, input().split())
num = list(map(int, input().split()))
num_candidate = list()

result = 0

for i in range(n) :
    a = 0
    for j in range(i+1, n) :
        for k in range(j+1, n) :
            a = num[i] + num[j] + num[k]
            if a <= m :
                num_candidate.append(a)

result = max(num_candidate)
print(result)