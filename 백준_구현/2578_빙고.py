import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
num_call = [list(map(int, input().split())) for _ in range(5)]

def bingo_check(r, c):
    cnt = 0
    # 가로체크
    for i in range(5):
        bingo = True
        n = board[i].count(0)
        if n == 5:
            cnt += 1
    # 세로체크
    for i in range(5):
        bingo = True
        for j in range(5):
            if board[j][i] != 0:
                bingo = False
                break
        if bingo:
            # print('ㅅㄹ')
            cnt += 1

    for i in range(5):
        if board[i][i] != 0:
            break
    else:
        # print('->ㅣ')
        cnt += 1
    
    for i in range(5):
        if board[i][4-i] != 0:
            break
    else:
        # print('<-l')
        cnt += 1
    # print(cnt)
    if cnt >= 3:
        return True


call_cnt = 0
bingo  = False
ans = 0
for i in range(5):
    for j in range(5):
        call = num_call[i][j]
        call_cnt += 1
        for x in range(5):
            for y in range(5):
                if board[x][y] == call:
                    board[x][y] = 0
                    # print(call_cnt)
                    # print()
                    bingo = bingo_check(x,y)
                    if bingo:
                        ans = call_cnt
                        print(ans)
                        # print(board)
                        exit()
    #         if bingo:
    #             break
    #     if bingo:
    #         break
    # if bingo:
    #     break

                    
# print(board)
            
# print('asd')
# print(ans, 1)