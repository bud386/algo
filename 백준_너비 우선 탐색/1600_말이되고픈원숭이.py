import sys
from collections import deque
input = sys.stdin.readline

K = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]

dr = [1, -1, 0, 0, -2, -2, -1, -1, 2, 2, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -2, 2, -1, 1, -2, 2]

visited = [[[0]*(K+1) for _ in range(w)] for _ in range(h)]
q = deque()
q.append([0, 0, 0, 0]) # 시작점, 말 이동, 총 이동

def bfs():
    while q:
        r, c, horse_move, cnt = q.popleft()
        
        if r == h-1 and c == w-1:
            # print(cnt)
            return cnt
            # break

        if horse_move < K:
            for i in range(12):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == 0:
                    if 3 < i < 12:
                        if visited[nr][nc][horse_move + 1] == 0:
                            visited[nr][nc][horse_move + 1] = cnt + 1
                            q.append([nr, nc, horse_move +1, cnt+1])
                    else:
                        if visited[nr][nc][horse_move] == 0:
                            visited[nr][nc][horse_move] = cnt + 1
                            q.append([nr, nc, horse_move, cnt+1])                    
                
        else:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == 0 and visited[nr][nc][horse_move] == 0:                
                    visited[nr][nc][horse_move] = cnt + 1
                    q.append([nr, nc, horse_move,  cnt + 1])

    return -1

print(bfs())
