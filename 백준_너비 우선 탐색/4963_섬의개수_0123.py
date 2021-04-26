import sys
from collections import deque

while True:
    # 맵의 크기
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h ==0:
        break

    # 섬의 위치 입력
    board = []
    for i in range(h):
            board.append(list(map(int, sys.stdin.readline().split())))
    # print(board)

    visited = [[0 for i in range(w)] for _ in range(h)]

    # 섬의 좌표 저장
    locations = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                locations.append((i,j))

    # print(locations)

    # 동서남북, 대각선 4경우
    dr = [0, 1, 0, -1, 1, 1, -1, -1 ]
    dc = [1, 0, -1, 0, 1, -1, 1, -1 ]
    
    q = deque()
    count = 0
    # 섬위 위치들에 대해서 각각 bfs
    for location in locations:
        # print(location, type(location), location[0])
        if visited[location[0]][location[1]] == 0:
            # 방문했다고 표시
            visited[location[0]][location[1]] = 1
            q.append(location)
            # print(f'시작{q}')
            while q:
                # print(f'다시{q}')
                now = q.popleft()
                # print(now)
                for i in range(8):
                    nextR = now[0] + dr[i]
                    nextC = now[1] + dc[i]
                    # print(nextR, nextC)
                    if 0 <= nextR < h and 0 <= nextC < w and visited[nextR][nextC] == 0 and board[nextR][nextC] == 1:
                        # print(nextR,nextC)
                        q.append((nextR,nextC))
                        visited[nextR][nextC] = 1
            count += 1
                
    print(count)


    # 첫번째 에러 dr, dc 잘못 만듬
    # 두번째 if 문에서 next <= h, w 해줌
    # location 할 때 맨첨엔 그냥 좌표를 바로 q에 집어넣고 for location in q 했는데
    # 이러면 나중에 while q: 하고 여기서 q.pop~ 할때 q가 변해서 오류가 남 (copy.deepcopy)? 이걸 잘 이용하거나 새로 만들어줘야함
    # 그래서 걍 locations 만들어서 좌표 저장해줌
    # 프린트는 한번만 하는게 좋다!!!
