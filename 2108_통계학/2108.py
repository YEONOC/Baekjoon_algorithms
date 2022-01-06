import sys

n = int(sys.stdin.readline())

num = []
for _ in range(n) :
    num.append(int(sys.stdin.readline()))

#1 산술평균
sum = 0
for i in range(n) :
    sum += num[i]
first = round(sum / n)

print(first)

#2 중앙값
num.sort()
second = num[n//2]

print(second)

#3 최빈값
aa = [0 for i in range(8000+1)]
for i in num :
    aa[i+4000] += 1

if aa.count(max(aa)) == 1:
    third = aa.index(max(aa)) - 4000

else :
    m = 0
    i = -1
    while m != 2 :
        i += 1
        if aa[i] == max(aa):
            m+=1
    third = i - 4000

print(third)
#4 범위
fourth = num[n-1] - num[0]

print(fourth)