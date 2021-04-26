import sys
input = sys.stdin.readline 

N = int(input())
schedule = []
ans = []

for i in range(N):
    start = i
    time, money = map(int, input().split())
    schedule.append([money, start, start+time]) # 수익, 시작일, 끝
    ans.append(money)


for i in range(N):  
    if schedule[i][2] <= N: # 남은 근무일안에 끝날때
        for j in range(schedule[i][2], N):  # end ~ N 까지 (i번째상담이 끝나는 날부터)
            if ans[i] + schedule[j][0] >= ans[j]:
                ans[j] = ans[i] + schedule[j][0]
    else:
        ans[i] = 0
print(max(ans))
