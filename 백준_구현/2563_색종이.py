import sys

# 전체 도화지 (100*100)
paper = [[0]*100 for i in range(100)]

n = int(sys.stdin.readline())

# 색종이가 들어가는 좌표 1로 표시 (10*10)
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[j][i] = 1

result = 0
for pap in paper:
    result += pap.count(1)
print(result)



