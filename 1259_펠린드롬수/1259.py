while True :
    n = int(input())
    pelinStat = True

    if n == 0 :
        break
    else :
        s_n = str(n)
        for i in range(len(s_n)//2) :
            if (s_n[i] != s_n[-(i+1)]) :
                print('no')
                pelinStat = False
                break
        if (pelinStat == True) :
            print('yes')