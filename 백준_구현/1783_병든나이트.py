import sys

n, m = map(int, sys.stdin.readline().split())

ans = 1

if n > 2:
    if m < 5:
        ans = m
    elif m == 5 or m == 6:
        ans = 4
    else: 
        ans = m - 2
elif n == 2:
    #2 1, 2 2, 2 3, 2 4, 2 5, 2 6
    if m < 7:
        ans = (m+1) // 2
    else:
        ans = 4

print(ans)

