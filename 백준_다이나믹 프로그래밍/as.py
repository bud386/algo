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


N = int(input())
row_visit = [0] * N     # 순열생성(방문한 row)
row_col = [0] * N       # 퀸의 위치

def possible(k, col):
    for i in range(k):
        # 대각선 확인(x3-x1)/(y3-y1) == 1, (x3-x2)/(y3-y2) == 1 (대각선의 기울기는 1)
        if k - i == abs(col - row_col[i]):
            return False
    return True

def NQueen(k):  # k번째 퀸
    global cnt
    if k == N:
        cnt += 1
        pass
    else:
        for i in range(N):
            if row_visit[i] or not possible(k, i):
                continue
            row_visit[i] = 1
            row_col[k] = i # k번째 퀸을 k행 i열에 배치
            NQueen(k+1)
            row_visit[i] = 0

cnt = 0
NQueen(0)
print(cnt)