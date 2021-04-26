import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
baby_shark = deque()
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            baby_shark.append([i, j, 2, 0]) # 좌표, size, 이동칸수
            board[i][j] = 0     # 상어가 이동할거니까 0으로 표시

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
ans = 0
eaten = 0   # 먹은 물고기 수

# for _ in range(10)
while baby_shark:

    visited = [[0]*N for _ in range(N)]
    eatable = []    # 먹을 수 있는 
    min_cnt = 9999
    # flag = True

    while baby_shark:
        x, y, size, cnt = baby_shark.popleft()  # 좌표, size, 이동칸수
        visited[x][y] = 1
        for i in range(4):
            r = x + dr[i]
            c = y + dc[i]
            if 0 <= r < N and 0 <= c < N and visited[r][c] == 0:
                
                if board[r][c] == 0 or board[r][c] == size: 
                    visited[r][c] = 1
                    baby_shark.append([r, c, size, cnt + 1])
                
                elif board[r][c] != 0:  
                    if board[r][c] < size:  # 사이즈가 작아 먹을 수 있다면
                        visited[r][c] = 1
                        min_cnt = min(min_cnt, cnt+1)   # 가장 가까운 거리
                        if cnt + 1 == min_cnt:  # 가장 가까운 거리에 있는 먹을 수 있는 물고기를 모두 eatable list에 저장
                            eatable.append([r, c, cnt+1])
                            ans = cnt + 1
                        else:   # 아니먄 탐색 중지
                            break
        
    if eatable:
        eatable = sorted(eatable, key = lambda x : (x[0], x[1]))    # 가장 위, 왼쪽 순으로 정렬
        board[eatable[0][0]][eatable[0][1]] = 0     # 맨 앞에 있는 물고기를 먹고 먹은 좌표 0으로 표시
        eaten += 1
        if eaten == size:   # 먹은 물고기수가 size만큼이면
            size += 1
            eaten = 0
        baby_shark = deque([[eatable[0][0], eatable[0][1], size, ans]])     # 잡아먹은 물고기의 좌표를 q 넣어줌
        # flag = False

    # if flag:
    #     break                                        
    
print(ans)                        



# q = deque([[]]) () 안에 [[]] 로 해야되는것 주의
