import sys

N, M = map(int, sys.stdin.readline().split())

box = []
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().strip())))

ans = []
short_side = M
if N < M:
    short_side = N

for i in range(N):
    for j in range(M):
        # 범위 바꾸ㅝ서 큰거부터 해줘서 시간단축!
        for k in range(1, short_side):
            if i+k < N and j+k < M:
                if box[i][j] == box[i][j+k] and box[i][j] == box[i+k][j] and box[i][j] == box[i+k][j+k]:
                    ans.append((k+1)**2)

if ans:
    print(max(ans))
else:
    print(1)









for i in range(0,0):
    for j in range(0,2):
        print(i,j)

import sys

N, M = map(int, sys.stdin.readline().split())

box = []
for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().strip())))

ans = []
short_side = min(N, M)

for i in range(N):
    for j in range(M):
        for k in range(1, short_side):
            if i+k >= N or j+k >= M:
                break
            else:
                if box[i][j] == box[i][j+k] and box[i][j] == box[i+k][j] and box[i][j] == box[i+k][j+k]:
                    ans.append((k+1)**2)

if ans:
    print(max(ans))
else:
    print(1)