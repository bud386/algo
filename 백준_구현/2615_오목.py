import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
visited = [[0] * 19 for _ in range(19)]
dr = [1, 1, 1, -1, -1, -1, 0, 0]
# 5 4 3
# 7 . 6
# 0 1 2
dc = [-1, 0, 1, 1, 0, -1, 1, -1]
winner = 0
ans = [0, 0]

for i in range(19):
    for j in range(19):
        if board[i][j] == 1 and visited[i][j] == 0:
            cnt_1 = 1
            visited[i][j] = 1
            for k in range(8):
                nextR = i + dr[k]
                nextC = j + dc[k]
                cnt_1 = 1
                if 0 <= nextR < 19 and 0 <= nextC < 19 and board[nextR][nextC] == 1 and visited[nextR][nextC] == 0:

                    while 0 <= nextR < 19 and 0 <= nextC < 19 and board[nextR][nextC] == 1 and visited[nextR][nextC] == 0:
                        cnt_1 += 1
                        # print(nextR, nextC, k, cnt_1)
                        # visited[nextR][nextC] = 1
                        nextR += dr[k]
                        nextC += dc[k]

                # print(i, j, cnt_1, k)
                if cnt_1 == 5:
                    # print(i, j, k)
                    if (k == 6 and 0<= j-1 < 19 and board[i][j - 1] != 1) or (k == 6 and j == 0):
                        winner = 1
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 0 and 0<= i + dr[k + 3] < 19 and 0<= j + dc[k + 3] < 19 and board[i + dr[k + 3]][j + dc[k + 3]] != 1) or (k == 0 and (i == 0 or j == 19)):
                        winner = 1
                        ans[0] = i + 5
                        ans[1] = j - 3
                        break
                    elif (k == 1 and 0<= i + dr[k + 3] < 19 and 0<= j + dc[k + 3] < 19 and board[i + dr[k + 3]][j + dc[k + 3]] != 1) or (k == 1 and i == 0):
                        winner = 1
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 2 and 0<= i + dr[k + 3] < 19 and 0<= j + dc[k + 3] < 19 and board[i + dr[k + 3]][j + dc[k + 3]] != 1) or (k == 2 and (i == 0  or j == 0)):
                        winner = 1
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
    
                         

        if board[i][j] == 2 and visited[i][j] == 0:
            cnt_2 = 1
            visited[i][j] = 1
            for k in range(8):
                nextR = i + dr[k]
                nextC = j + dc[k]
                cnt_2 = 1
                if 0 <= nextR < 19 and 0 <= nextC < 19 and board[nextR][nextC] == 2 and visited[nextR][nextC] == 0:
                    
                    while 0 <= nextR < 19 and 0 <= nextC < 19 and board[nextR][nextC] == 2 and visited[nextR][nextC] == 0:
                        cnt_2 += 1
                        nextR += dr[k]
                        nextC += dc[k]

                if cnt_2 == 5:
                    # print('k', k)
                    if (k == 6 and 0<= j-1 < 19 and board[i][j - 1] != 2) or (k == 6 and j == 0):
                        # print(board[i + dr[k + 3]][j + dc[k + 3]], k )
                        winner = 2
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 0 and 0<= i + dr[k + 3] < 19 and 0<= j + dc[k + 3] < 19 and board[i + dr[k + 3]][j + dc[k + 3]] != 2) or (k == 0 and (i == 0 or j == 19)):
                        # print(board[i + dr[k + 3]][j + dc[k + 3]])
                        winner = 2
                        ans[0] = i + 5
                        ans[1] = j - 3
                        break
                    elif (k == 1 and 0<= i + dr[k + 3] < 19 and 0<= j + dc[k + 3] < 19 and board[i + dr[k + 3]][j + dc[k + 3]] != 2) or (k == 1 and i == 0):
                        # print(board[i + dr[k + 3]][j + dc[k + 3]])
                        winner = 2
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 2 and 0<= i + dr[k + 3] < 19 and 0<= j + dc[k + 3] < 19 and board[i + dr[k + 3]][j + dc[k + 3]] != 2) or (k == 2 and (i == 0  or j == 0)):
                        # print(board[i + dr[k + 3]][j + dc[k + 3]])
                        winner = 2
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break

print(winner)
if winner != 0:
    print(*ans)

