from collections import deque

n, k = map(int, input().split())

board = [0]*100001
board[n] = 1
board[k] = k

visited = [0]*100001

q = deque()
q.append((n,0))

move = [1,-1, 2]
ans = []

while q :
    now = q.popleft()

    for i in range(3) :
        if i == 0 or i ==1:
            next = now[0]+move[i]
        else:
            next = now[0]*move[i]
        
        if 0<=next<100001 and visited[next]==0 and board[next]==0 :
            q.append((next, now[1]+1))
            visited[next]= 1
            # print(now)
            
        if 0<=next<100000 and visited[next]==0 and board[next]==k :
            ans.append(now[1])
            
        
print(min(ans)+1)