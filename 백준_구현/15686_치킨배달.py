import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _  in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

chicken = []
house = []
chicken_cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i, j])
            chicken_cnt += 1
        elif board[i][j] == 1:
            house.append([i, j])

ans = 99999999
pick = []
def combi(start):
    global chicken_cnt, M, ans
    if len(pick) == M:
        total = 0        
        for r1, c1 in house:
            dist = 99999999
            for r2, c2 in pick:
                dist = min(dist, abs(r1-r2) + abs(c1-c2))
            total += dist
        ans = min(ans, total)        
        return
    for i in range(start, chicken_cnt):
        pick.append(chicken[i])
        combi(i+1)
        pick.pop()

combi(0)
print(ans) 



