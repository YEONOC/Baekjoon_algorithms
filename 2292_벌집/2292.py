n = int(input())
i = 1
a = 2
while(True) :
    if(n < 2) :
        print(1)
        break
    elif (a <= n < a+6*i) :
        print(i+1)
        break
    a = a+6*i
    i += 1