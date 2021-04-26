N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split(" "))))

ans = [0 for i in range(N+1)]


def solution():
    # 뒤에서 부터 dp 시작 N - Tn 이 0 초과면 불가능
    #  for 문 n부터 0으로
    for i in range(N-1, -1, -1):
        if i + arr[i][0] > N:  # 상담이 불가능한 부분 확인(마지막상담)
            ans[i] = 0
        else:
            ans[i] = max(arr[i][1] + max(ans[i+arr[i][0]:]), ans[i+arr[i][0]])
            #            현재P값        T값 이후 부터 최대값       T값 직후 값
    print(ans)
    print(max(ans))
solution()