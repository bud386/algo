import sys
input = sys.stdin.readline

N, M = map(int, input().split())
times = list(map(int, input().split()))

start =  min(times)
end = min(times) * M

while start <= end:
    total = 0
    mid  = (start + end) // 2
    for time in times:
        total += mid // time

    if total >= M:
        end = mid - 1
    else:
        start = mid + 1

print(end+1)