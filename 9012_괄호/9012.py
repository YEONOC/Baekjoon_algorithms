def vps(v) :
    stack = []
    result = 'YES'
    for i in range(len(v)) :
        if (v[i] == '(') :
            stack.append(v[i])
        elif (v[i] == ')') :
            if (len(stack) == 0) :
                result = 'NO'
            else :
                del stack[len(stack) - 1]
    if (len(stack) != 0) :
        result = 'NO'
    return result

n = int(input())

for _ in range(n) :
    v = input()
    print(vps(v))