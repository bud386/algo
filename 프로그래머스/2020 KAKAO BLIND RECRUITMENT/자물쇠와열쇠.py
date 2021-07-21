# 자물쇠보다 키가 더 작다?
# 90도 회전
def rotate(key, M):        
    new_key = [[0] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[j][M-1-i] = key[i][j] 
    return new_key

def move(M, N, key, move_key, ):
    for i in range(4):            
        for r in range(M):
            for c in range(M):    
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    move_key[nr][nc] = key[r][c]
        for 
    
def solution(key, lock):
    answer = True
    M = len(key)
    N = len(lock)
    slot = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 1:
                slot.append([i,j])
                
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # 90도 회전
    key = rotate(key, M)
    move_key = [[0] for _ in range(M)]
    
    for _ in range(4):
        key = rotate(key, M)
        
        for i in range(4):            
            for r in range(M):
                for c in range(M):    
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        move_key[nr][nc] = key[r][c]
            
                
                
    return answer