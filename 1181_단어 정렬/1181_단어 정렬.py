n = int(input())
worddic = dict()

for i in range(n):
    word = input()
    length = len(word)
    if length in worddic:
        worddic[length].append(word)
    else:
        worddic[length] = [word]

for i in sorted(worddic.items()):
    sortlist = sorted(list(set(i[1])))
    for j in sortlist:
        print(j)