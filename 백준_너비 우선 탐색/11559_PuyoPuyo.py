import sys
from collections import deque
input = sys.stdin.readline

board = []
for _ in range(12):
    puyo = list(input().strip())
    board.append(puyo)

ans = 0
colors = ['R', 'G', 'B', 'P', 'Y']
q = deque()

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    cnt = 1
    loc = [[r, c]]
    while q:
        r, c, puyo = q.popleft()        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 12 and 0 <= nc < 6 and visited[nr][nc] == 0:                
                if board[nr][nc] == puyo:
                    visited[nr][nc] = 1
                    cnt += 1
                    q.append([nr, nc, puyo])
                    loc.append([nr, nc])    
    if cnt >= 4:
        return loc
    else:
        return False

while True:
    visited = [[0]*6 for _ in range(12)]
    flag = False
    for i in range(12):
        for j in range(6):
            if board[i][j] in colors and visited[i][j] == 0:
                visited[i][j] = 1
                q.append([i,j, board[i][j]])
                boom = bfs(i, j)

                if boom:
                    flag = True
                    for x, y in boom:
                        board[x][y] = ''
    
    # 뿌요가 터진적이 없으면
    if flag == False:
        break
    ans += 1

    # 밑에서 부터 한칸식 내리기
    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] == '':
                r = i
                while 0 <= r and board[r][j] == '':
                    r -= 1
                if r == -1:
                    for k in range(0, i+1):
                        board[k][j] = '.'
                else:
                    board[i][j] = board[r][j]
                    board[r][j] = ''


print(ans)
