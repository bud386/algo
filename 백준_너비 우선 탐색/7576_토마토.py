import sys
from collections import deque

n,m = map(int, input().split())

board=[]

# 상자 생성
for i in range(m) :
    board.append(list(map(int, input().split())))

q = deque()
visited = [[0 for _ in range(n)] for _ in range(m)]
# print(visited)

# 오른쪽, 아래, 왼쪽, 위쪽
dr = [0, 1, 0, -1] 
dc = [1, 0, -1, 0]
#토마토 수
cnt_tomato = 0
# 토마토 없는 칸 수
cnt_empty = 0

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i,j,0))
            cnt_tomato += 1
        elif board[i][j] == -1:   
            cnt_empty += 1

while q :
    now = q.popleft()
#     print(f'now ={now}')

    for i in range(4) :
        
        nextR, nextC = now[0]+dr[i],now[1]+dc[i]
#         print(f'r= {nextR}, c= {nextC}')
        
        if 0<=nextR<m and 0<=nextC<n and visited[nextR][nextC]==0 and board[nextR][nextC]==0 :
            q.append((nextR, nextC, now[2]+1))
#             print(q)
            visited[nextR][nextC]=now[2]+1
#             print(visited)
#             print()

# visited에서 0의 개수
cnt_zero = 0
for i in visited:
    for j in i:
        if j == 0:
            cnt_zero += 1
# print(visited)            
# print(cnt_zero, cnt_tomato, cnt_empty)
            
if cnt_tomato == m*n:
    print(0)
elif cnt_zero > (cnt_tomato  + cnt_empty):
    print(-1)
else:
    print(now[2])