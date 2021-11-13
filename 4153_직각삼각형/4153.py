while(True) :
    longs = list(map(int, input().split()))
    
    c = max(longs)
    longs.remove(c)
    a = min(longs)
    longs.remove(a)
    b = longs[0]
    if (a == 0 and b == 0 and c == 0) :
        break
    else :
        if (a**2 + b**2 == c**2) :
            print("right")
        else :
            print("wrong")