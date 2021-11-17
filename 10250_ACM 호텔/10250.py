t = int(input())

for i in range(t) :
    h, w, n = map(int, input().split())

    num = 1
    if(h >= n) :                # 주어진 n이 h보다 작으면
        num += 100 * n          # XX01호를 정해준다
    else :                      # 주어진 n이 h보다 크면
        a = n % h               # a는 XX를 알기 위해 n이 h층을 몇 번 지났는지
        b = n // h              # b는 YY를 알기 위해
        if (a == 0) :           # a가 0일때는 n이 h층 일때
            num += 100 * h
            num -= 1
        else :
            num += 100 * a

        num += 1 * b            #YY 산출

    print(num)