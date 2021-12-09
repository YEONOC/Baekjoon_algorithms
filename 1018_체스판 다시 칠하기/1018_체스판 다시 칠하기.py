def chk(chkboard, fix) :
    fixb = 0
    fixw = 0
    for j in range(8) :
        for k in range(8) :
            if ((j % 2 == 0) and (k % 2 == 0)) or ((j % 2 == 1) and (k % 2 == 1)) :
                if (chkboard[j][k] != 'B') :
                    fixb += 1
            else :
                if (chkboard[j][k] != 'W') :
                    fixb += 1
    for j in range(8) :
        for k in range(8) :
            if ((j % 2 == 0) and (k % 2 == 0)) or ((j % 2 == 1) and (k % 2 == 1)) :
                if (chkboard[j][k] != 'W') :
                    fixw += 1
            else :
                if (chkboard[j][k] != 'B') :
                    fixw += 1
    fix = min(fixb, fixw)
    return fix

def mkchkboard(b, c, chkboard, board) :
    cc = c
    for j in range(8) :
        for k in range(8) :
            chkboard[j][k] = board[b][cc]
            cc += 1
        b += 1
        cc = c
    return chkboard

n, m = map(int, input().split())
board = list()

for i in range(n) :
    board.append(input())

a = (n - 7) * (m - 7)
b = 0
c = 0
candidate_fix = list()
chkboard = [[0 for i in range(8)] for j in range(8)]


for z in range(a) :
    fix = 0
    chkboard = mkchkboard(b, c, chkboard, board)
    candidate_fix.append(chk(chkboard, fix))
    if (b + 8 == n) :
        c += 1
        b = 0
    else :
        b += 1

print(min(candidate_fix))