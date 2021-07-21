import sys
input = sys.stdin.readline

N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

start = 1
end = max(budgets)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for budget in budgets:
        if budget >= mid:
            total += mid
        else:
            total += budget
    
    if total > M:  # 예산 초과
        end = mid - 1   
    else:
        start = mid + 1

print(end)