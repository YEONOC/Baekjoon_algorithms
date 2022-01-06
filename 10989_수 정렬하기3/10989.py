import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

num = [0] * 10001
for _ in range(n):
    num[int(input())] += 1

for i in range(10001):
    for j in range(num[i]):
        print("%s\n" %i)