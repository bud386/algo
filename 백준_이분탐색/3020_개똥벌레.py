import sys
input = sys.stdin.readline

N, H = map(int, input().split())

b_h = []    # 석순
t_h = []    # 종유석
h = []
for i in range(N):
    if i%2:
        t_h.append(int(input()))
    else:
        b_h.append(int(input()))

# print(b_h, t_h)

h = 0
ans = []
min_cnt = 99999999
while h<=H:
    # print(h,'h')
    cnt = 0
    for i in range(N//2):
        if h <= b_h[i]:
            cnt += 1
        if H-h <= t_h[i]:
            cnt += 1
    if cnt <= min_cnt:
        ans.append(cnt)
        min_cnt = cnt
    h += 1
print(min_cnt, ans.count(min_cnt))


# start = min(b_h + t_h)
# end = max(b_h + t_h)
# while start <= end:
#     cnt = 0 
#     mid = (start + end) // 2
#     for i in range(N//2):
#         if mid <= b_h[i]:
#             cnt += 1
#         if H-mid <= t_h[i]:
#             cnt += 1
import sys

input = sys.stdin.readline

n, height = map(int, input().split())

col = [int(input()) for _ in range(n)]
a = col[0:n:2]
b = col[1:n:2]

a.sort()
b.sort(reverse=True)

cnt = len(a)
i, j = 0, 0
ans = n
ansCnt = 1
for h in range(1, height+1):

    while i<len(a):
        if a[i] < h:
            cnt -= 1
            i += 1
        else: break

    h = height-h
    while j<len(b):
        if b[j] > h:
            cnt += 1
            j += 1
        else: break

    if ans < cnt: continue
    elif ans == cnt:
        ansCnt += 1
    else:
        ans = cnt
        ansCnt = 1
print(ans, ansCnt)