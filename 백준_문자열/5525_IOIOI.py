import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

ans = cnt = idx = 0
while idx < m-2:
    if s[idx] == 'I' and s[idx+1] == 'O' and s[idx+2] == 'I':
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
        idx += 2
    else:
        cnt = 0
        idx += 1

print(ans)