import sys

n = int(sys.stdin.readline())

# 찾아야 하는 숫자
m = int(sys.stdin.readline())

table = [[0]*n for _ in range(n)]
ans = [0,0]


start_idx = n//2
now = [start_idx, start_idx]
table[now[0]][now[1]] = 1

num = 2

for i in range(1, n):
    if i % 2:
        for _ in range(i):
            now[0] -= 1
            table[now[0]][now[1]] = num
            if num == m:
                ans[0], ans[1] = now[0], now[1]
            num += 1
        for _ in range(i):
            now[1] += 1
            table[now[0]][now[1]] = num
            if num == m:
                ans[0], ans[1] = now[0], now[1]
            num += 1
    else:
        for _ in range(i):
            now[0] += 1
            table[now[0]][now[1]] = num
            if num == m:
                ans[0], ans[1] = now[0], now[1]
            num += 1
        for _ in range(i):
            now[1] -= 1
            table[now[0]][now[1]] = num
            if num == m:
                ans[0], ans[1] = now[0], now[1]
            num += 1
            
for i in range(n-2, -1, -1):
    table[i][0] = num
    now[0], now[1] = i, 0
    if num == m:
        ans[0], ans[1] = now[0], now[1]
    num += 1

for row in table:
    print(*row)
print(ans[0]+1, ans[1]+1)

