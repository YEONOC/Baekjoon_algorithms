def balance(s) :
    len_s = len(s)
    result = 'yes'
    stack = []
    for i in range(len_s) :
        if (s[i] == '(') :
            stack.append([s[i], 0])
        elif (s[i] == '[') :
            stack.append([s[i], 1])
        elif s[i] == ')' :
            if len(stack) == 0 or (stack[len(stack) - 1][1] != 0) :
                result = 'no'
            else :
                del stack[len(stack) - 1]
        elif s[i] == ']' :
            if len(stack) == 0 or (stack[len(stack) - 1][1] != 1) :
                result = 'no'
            else :
                del stack[len(stack) - 1]
    if (len(stack) != 0) :
        result = 'no'
    return result

s = ''

while s != '.' :
    s = input()
    if (s == '.') :
        break
    else :
        print(balance(s))