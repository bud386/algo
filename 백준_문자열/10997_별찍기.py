import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print('*')
    exit()

h = 4*n-1   # 세로 길이
w = 4*n-3   # 가로 길이
s = [[' '] * w for _ in range(h)]

nr = 0  # 시작 row
nc = 4*n-3 -1   # 시작 col
s[nr][nc] = '*'

# 순서: 왼쪽, 아래, 오른쪽, 위
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

flag = False

while True:
    for i in range(4):
        nr += dr[i]
        nc += dc[i]
        while (0<= nr < h and 0 <= nc < w) and s[nr][nc] == ' ':
            s[nr][nc] = '*'
            nr += dr[i]
            nc += dc[i]
        
        if nr == -1 or nc == -1 or nr == h or nc == w:
            nr -= dr[i]
            nc -= dc[i]
        else:
            nr -= dr[i]
            nc -= dc[i]
            s[nr][nc] = ' '
            nr -= dr[i]
            nc -= dc[i]
        if s[2*n][2*(n-1)] == '*': # 마지막에 방문할 부분
            flag = True
            break  

    if flag:
        break     

for i in range(h):    
    print(''.join(s[i]).strip())
