kg = int(input())
num = list([-1])

for i in range((kg // 5) + 1) :
    for j in range((kg // 3) + 1) :
        if (i * 5 + j * 3 == kg) :
            num.append(i + j)
            num[0] = num[1]

print(min(num))