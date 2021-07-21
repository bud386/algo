import sys
input = sys.stdin.readline
from collections import deque

# 총 F층, 현재 S, 목적지 G
F, S, G, U, D = map(int, input().split()) 

q = deque()
q.append([S, 0])
visited = [0]* (F+1)
visited[S] = 1

up_down = [U, -D]

ans = 'use the stairs'
while q:
    now, cnt = q.popleft()
    if now == G:
        ans = cnt
        break
    for i in range(2):
        next = now + up_down[i]
        if next < 1 or next > F:
            next = now
        if visited[next] == 0:
            visited[next] = 1
            q.append([next, cnt + 1])

print(ans)