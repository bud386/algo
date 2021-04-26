import sys
input = sys.stdin.readline

N = int(input())
marble = list(map(int, input().split()))

permN = N -2    # pop 가능한 인덱스 1 ~ N-2까지
pop_idx = [i for i in range(1, N-1)]    # pop(삭제) 가능한 인덱스 1 ~ N-2까지
order = [0] * (permN)   # 생성한 순열 저장
visit = [0] * (permN)   # 중복 체크

max_ans = 0

# 중복없는 순열 생성
def perm(idx, ans):
    global max_ans

    if idx == permN:
        marble_visited = [0] * N    # 제거한 구슬을 표시할 리스트
        for i in order:            
            marble_visited[i] = 1 # 구슬 제거
            l = i 
            r = i 
            while marble_visited[l] == 1: # 제가하지 않은 구슬을 만날때까지
                l -= 1
            while marble_visited[r] == 1: 
                r += 1            
            ans += (marble[l] * marble[r])            
        max_ans = max(ans, max_ans)

    else:
        for i in range(permN):
            if visit[i]: continue
            order[idx] = pop_idx[i]
            visit[i] = 1
            perm(idx + 1, 0)
            visit[i] = 0

perm(0, 0)
print(max_ans)



