import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]
# visited = [[0] * 19 for _ in range(19)]
dr = [1, 1, 1, 0, -1, -1, -1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]
# 6 5 4
# 7 x 3
# 0 1 2
winner = 0
ans = [0, 0]

for i in range(19):
    for j in range(19):
        if board[i][j] == 1:
            for k in range(4):
                cnt_1 = 1
                nextR = i + dr[k]
                nextC = j + dc[k]
                while 0 <= nextR < 19 and 0 <= nextC < 19 and board[nextR][nextC] == 1:
                    cnt_1 += 1            
                    nextR += dr[k]
                    nextC += dc[k]

                if cnt_1 == 5:                    
                    if (k == 3 and 0<= j-1 < 19 and board[i][j - 1] != 1) or (k == 3 and j == 0):
                        winner = 1
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 0 and 0<= i + dr[k + 4] < 19 and 0<= j + dc[k + 4] < 19 and board[i + dr[k + 4]][j + dc[k +4]] != 1) or (k == 0 and (i == 0 or j == 19)):
                        winner = 1
                        ans[0] = i + 5
                        ans[1] = j - 3
                        break
                    elif (k == 1 and 0<= i + dr[k + 4] < 19 and 0<= j + dc[k + 4] < 19 and board[i + dr[k + 4]][j + dc[k + 4]] != 1) or (k == 1 and i == 0):
                        winner = 1
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 2 and 0<= i + dr[k + 4] < 19 and 0<= j + dc[k + 4] < 19 and board[i + dr[k + 4]][j + dc[k + 4]] != 1) or (k == 2 and (i == 0  or j == 0)):
                        winner = 1
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
    
                         

        if board[i][j] == 2:
            for k in range(4):
                cnt_2 = 1
                nextR = i + dr[k]
                nextC = j + dc[k]                            
                while 0 <= nextR < 19 and 0 <= nextC < 19 and board[nextR][nextC] == 2:
                    cnt_2 += 1
                    nextR += dr[k]
                    nextC += dc[k]

                if cnt_2 == 5:
                    if (k == 3 and 0<= j-1 < 19 and board[i][j - 1] != 2) or (k == 3 and j == 0):
                        winner = 2
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 0 and 0<= i + dr[k + 4] < 19 and 0<= j + dc[k + 4] < 19 and board[i + dr[k + 4]][j + dc[k + 4]] != 2) or (k == 0 and (i == 0 or j == 19)):
                        winner = 2
                        ans[0] = i + 5
                        ans[1] = j - 3
                        break
                    elif (k == 1 and 0<= i + dr[k + 4] < 19 and 0<= j + dc[k + 4] < 19 and board[i + dr[k + 4]][j + dc[k + 4]] != 2) or (k == 1 and i == 0):                        
                        winner = 2
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break
                    elif (k == 2 and 0<= i + dr[k + 4] < 19 and 0<= j + dc[k + 4] < 19 and board[i + dr[k + 4]][j + dc[k + 4]] != 2) or (k == 2 and (i == 0  or j == 0)):                        
                        winner = 2
                        ans[0] = i + 1
                        ans[1] = j + 1
                        break

print(winner)
if winner != 0:
    print(*ans)

