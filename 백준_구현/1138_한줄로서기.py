import sys

N = int(sys.stdin.readline())
counts = list(map(int, sys.stdin.readline().split()))

ans = [0] * N

ans[counts[0]] = 1

cnt_zero = 0
for i in range(1, N):
    for j in range(len(ans)):
        if ans[j] == 0:
            cnt_zero += 1
        if cnt_zero == counts[i]+1:
            ans[j] = i + 1
            cnt_zero = 0
            break
                
print(*ans)







# import heapq
# N = int(input())
# arr = [[idx, val] for idx, val in enumerate(map(int, input().split()), 1)]
# ans = []
# print(arr)
# for idx, val in arr[::-1]:
#     print(idx, val)
#     ans.insert(val, idx)
#     print(ans)
# print(*ans)