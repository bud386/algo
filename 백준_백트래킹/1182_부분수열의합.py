import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0
for i in range(1, 1<<N): # 공집합은 제외
    total = 0
    for j in range(N):
        if i & (1 << j):
            total += nums[j]        
    if total == S:
        ans += 1

print(ans)