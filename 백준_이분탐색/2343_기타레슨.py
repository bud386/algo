import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lesson = list(map(int, input().split()))
lesson.sort()
print(N,M, lesson)
ans = lesson[N-1]
# cnt = 99999
total = 0
k=1
cnt = 0
while True:
    print(ans, cnt)
    for i in lesson:
        total += i
        if total > ans:
            cnt += 1
            total = i
        elif total == ans:
            cnt += 1
            total = 0
        if cnt > M:
            print(cnt, M, total, ans)
            # k +=1
            # ans += sum(lesson[N-k:N])
            ans += 1
            cnt= 1
            break
    else:
        # print(cnt, M)
        break
        

print(ans)

# sum(lesson[N-k:N])