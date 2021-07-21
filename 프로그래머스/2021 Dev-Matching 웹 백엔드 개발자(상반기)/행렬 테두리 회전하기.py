rows = int(input())
columns = int(input())
board = []
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
queries =[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
cnt = 1
ans = []
for i in range(rows):
    board.append([j for j in range(cnt, cnt + columns)])
    cnt += columns
# print(board)
# print(len(board), len(board[0]))
for query in queries:
    tmp = [[0]*columns for _ in range(rows)]
    r1, c1, r2, c2 = query
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    # print(len(tmp), len(tmp[0]))
    # 위
    for i in range(c1, c2):    
        tmp[r1][i+1] = board[r1][i]
    # 오른쪽
    for i in range(r1, r2):
        # print(i+1, c2, i)
        # print(tmp, board)
        tmp[i+1][c2] = board[i][c2]
    # 아래
    for i in range(c2, c1, -1):
        tmp[r2][i-1] = board[r2][i]
    # 왼쪽
    for i in range(r2, r1, -1):
        tmp[i-1][c1] = board[i][c1]
    
    min_num = 999999
    for r in range(rows):
        for c in range(columns):
            if tmp[r][c] != 0:
                board[r][c] = tmp[r][c]
                if min_num > tmp[r][c]:
                    min_num = tmp[r][c]
    ans.append(min_num)


print(ans)


