import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = [i, j]
        if board[i][j] == 'B':
            blue = [i, j]

q = deque()
q.append(red+blue+[1])        

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

def move(r, c, dr, dc):
    move_cnt = 0
    while board[r+dr][c+dc] != '#':
        # 구멍으로 탈출할 경우 0,0 return
        if board[r+dr][c+dc] == 'O':
            return 0, 0, 0
        r += dr
        c += dc
        move_cnt += 1
    return r, c, move_cnt

visit = {}
visit[red[0],red[1], blue[0], blue[1]] = 1
# cnt = 0
flag = 0
ans = -1
while q:
    rr, rc, br, bc, cnt= q.popleft()
    print(rr, rc, br, bc, cnt)
    if cnt > 10:
        ans = -1
        break    
    for i in range(4):
        nrr, nrc, r_cnt = move(rr, rc, dr[i], dc[i])
        nbr, nbc, b_cnt = move(br, bc, dr[i], dc[i])

        if nbc == 0 and nbr == 0: # 파란공 탈출 (or 동시탈출)
            continue

        elif nrr == 0 and nrc == 0: # 빨간공만 탈출
            ans = cnt
            flag = 1
            break

        if nrr == nbr and nrc == nbc:   # 공이 겹쳤을때 더 많이 움직인 공을 뒤로 보낸다.
            if r_cnt > b_cnt: 
                nrr -= dr[i]
                nrc -= dc[i]
            else:
                nbr -= dr[i]
                nbc -= dc[i]

        if (nrr, nrc, nbr, nbc) not in visit:
            visit[nrr, nrc, nbr, nbc] = 1
            q.append([nrr, nrc, nbr, nbc, cnt+1])
    if flag:
        break
    
print(ans)
