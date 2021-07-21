import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)

while start <= end:
    total = 0
    mid = (start + end) // 2    # 비트연산  >> 1
    for tree in trees:
        if tree - mid > 0:  # 변수에 담기
            total += (tree - mid)
    if total >= M:
        start = mid + 1
    else:
        end = mid -1

print(end)
