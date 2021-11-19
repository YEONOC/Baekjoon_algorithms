l = int(input())
s = input()
s_i = list()
answer = 0

for i in range(l) :
    s_i.append(ord(s[i]) - ord('a') + 1)

for i in range(l) :
    answer += s_i[i] * (31**i)

answer = answer % 1234567891
print(answer)