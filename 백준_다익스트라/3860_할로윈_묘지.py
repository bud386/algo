import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize 

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    board = [[1]*W for _ in range(H)]

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    G = int(input())
    for _ in range(G):
        X, Y = map(int, input().split())
        board[Y][X] = 'rip'

    E = int(input())
    ghost_hole = [[0]*W for _ in range(H)]
    for _ in range(E):
        X1, Y1, X2, Y2, T = map(int, input().split())
        # ghost_hole[Y1].append((Y2, X2))
        ghost_hole[Y1][X1] = [Y2, X2]
        # ghost_hole.append([X1, Y1, X2, Y2, T])
        board[Y1][X1] = T

    que = deque([[0, 0]]) 
    visited = [[0]*W for _ in range(H)]
    while que:
        r, c = que.popleft()
        if r == H -1 and c == W - 1:
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != 'rip' and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if ghost_hole[nr][nc] != 0: # 여기 귀신구멍이면
                    # print(w, '?', nr, nc)
                    que.append((ghost_hole[nr][nc][0], ghost_hole[nr][nc][1])) # 
                else:
                    que.append((nr, nc))

    # print(visited, 'visited')
    if visited[H-1][W-1] == 0:
        print('Impossible')

    else:
        q = [[board[0][0], 0, 0]]
        cnt = 0
        ans = 0
        while q:
            cnt += 1
            w, r, c = heappop(q)

            if r == H -1 and c == W - 1:
                # ans = w
                # print(ans)
                print(w)
                break
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < H and 0 <= nc < W and board[nr][nc] != 'rip':
                    if ghost_hole[nr][nc] != 0:
                        # print(w, '?', nr, nc)
                        heappush(q, (w+board[nr][nc], ghost_hole[nr][nc][0], ghost_hole[nr][nc][1]))
                    else:
                        heappush(q, (w+board[nr][nc], nr, nc))
            if cnt > (H*W)**2:
                print('Never')
                break

        # print(board)
        # print(ghost_hole)
        # print(ans)
