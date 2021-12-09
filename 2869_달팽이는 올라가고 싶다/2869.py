import math

a, b, v = map(int, input().split())

i = 0
i = (v-b) / (a - b)

print(math.ceil(i))