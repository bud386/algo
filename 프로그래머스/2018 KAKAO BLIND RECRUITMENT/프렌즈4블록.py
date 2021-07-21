def solution(m, n, board):
    answer = 0
    new_board = [list(i) for i in board]
    cnt = 0
    
    while True:
        flag = True # 지워지는 블럭 있는지 판단
        check = [[0]*n for _ in range(m)] # 지워질 블럭들 체크
        for i in range(m-1):
            for j in range(n-1):
                if new_board[i][j]:                
                    if new_board[i][j] == new_board[i+1][j] == new_board[i+1][j+1] == new_board[i][j+1]:
                        flag = False
                        # 지워지지 않은 블럭들일때 만 카운트
                        if check[i][j] == 0:
                            check[i][j] = 1
                            cnt += 1
                        if check[i+1][j] == 0:
                            check[i+1][j] = 1
                            cnt += 1
                        if check[i][j+1] == 0:
                            check[i][j+1] = 1
                            cnt += 1
                        if check[i+1][j+1] == 0:
                            check[i+1][j+1] = 1
                            cnt += 1
        
        if flag: # 더이상 지울 블럭이 없을때
            break
            
        # 지워져서 빈공간인 곳들은 0으로
        for i in range(m):  
            for j in range(n):
                if new_board[i][j] and check[i][j]:
                    new_board[i][j] = 0

        # 밑에서부터 빈공간 채우기
        for i in range(m-1, 1, -1):
            for j in range(n):
                if new_board[i][j] == 0:
                    k = 0
                    while True:
                        if i-k >= 1 and new_board[i-k][j] == 0:                    
                            k += 1                
                        else:
                            break
                    new_board[i][j] = new_board[i-k][j]
                    new_board[i-k][j] = 0 

    return cnt
                

# board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
# solution(6, 6, board)
