# N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
def solution(N, stages):
    answer = []
    n = len(stages) # 총 사용자
    challenger = [0] * N # 스테이지별 총 도전자
    fail_cnt = [0] * (N + 1) # 스테이지별 실패자
    fail_rate = {}
    for i in stages: # 현재 도전중인 스테이지
        i -= 1
        fail_cnt[i] += 1
    
        for j in range(N):            
            if i >= j:
                challenger[j] += 1                                        
                
    for i in range(N):
        if challenger[i] == 0:
            fail_rate[i+1] = 0
            continue
        fail_rate[i+1] = fail_cnt[i] / challenger[i]
    print(challenger, fail_cnt)    
    print(fail_rate)
    new_rate = sorted(fail_rate.items(), key=lambda x:(x[1], -x[0]), reverse=True)
    for stage in new_rate:
        answer.append(stage[0])
    print(answer)
    return answer


solution(4, [4, 4,4, 4])