def solution(board, moves):
    answer = 0    
    basket = []
    n = len(board)
    for i in moves:
        i -= 1                
        for j in range(n):
            if board[j][i]:
                basket.append(board[j][i])
                board[j][i] = 0
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2
                break
    
    return answer


    
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
solution(board, moves)
set()