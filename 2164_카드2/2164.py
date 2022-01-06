'''
#리스트 이용 (시간초과)
import sys
n = int(sys.stdin.readline())

que = []

for i in range(1, n+1) :
    que.append(i)

while len(que) != 1:
    i = 0
    que.pop(i)
    move=que[0]
    for j in range(1, len(que)) :
        que[j-1] = que[j]
    que[len(que)-1] = move

print(que)
'''
'''
#deque이용 (성공)
from collections import deque

d = deque()

for i in range(int(input())) :
    d.append(i+1)

while(len(d) != 1) :
    d.popleft()
    d.rotate(-1)

print(*d)
'''

#균형잡힌 세상

