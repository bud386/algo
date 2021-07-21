import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(i, cnt):
    global answer
    k = nums[i] - 1 # 선택학생
    # print(k+1, '학생', visited[k])
    if group[i] or group[k]:
        return
    # 사이클 판단
    if visited[k] == 0:    
        visited[k] = 1
        dfs(k, cnt + 1)
    else:
        if cnt > 1:
            check = k
            # 사이클을 돌아서 자기 자신까지 올때까지
            # print(check, i, cnt, group, visited)
            while i != check:
                if group[check]:
                    break
                group[i] = 1
                group[check] = 1
                answer += 1
                check = nums[check] - 1

            # team = copy.deepcopy(cnt)
            # answer += team
            return answer
        


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    # 자기 자신을 뽑은 사람
    group = [0] * n
    self_cnt = 0
    for i in range(n):
        if i == nums[i] - 1:
            group[i] = 1
            self_cnt += 1
    
    answer = 1
    visited = [0]*n
    for i in range(n):
        if group[i] or visited[i]:
            continue
        visited[i] = 1        
        print(i+1, '차례')
        dfs(i, 1)
        # print(answer+self_cnt,'누적')
    
    print(answer, self_cnt)
    print(n-answer-self_cnt)
    if answer > 1:
        print(n-answer-self_cnt, '정답')
    else:
        print(n-self_cnt, '정답')



# import sys 

# testcase = int(sys.stdin.readline()) 
# for _ in range(testcase): 
#     n = int(sys.stdin.readline()) 
#     choice = [0] + list(map(int, sys.stdin.readline().split())) 
#     visit = [0] * (n+1) 
#     group = 1 
#     for i in range(1, n+1): 
#         if visit[i] == 0: 
#             while visit[i] == 0: 
#                 visit[i] = group 
#                 i = choice[i] 
#             while visit[i] == group: 
#                 visit[i] = -1 
#                 i = choice[i] 
#             group += 1 
    
#     cnt = 0         
#     for v in visit: 
#         if v > 0: 
#             cnt += 1 
            
#     sys.stdout.write("{}\n".format(cnt))

# 출처: https://suri78.tistory.com/128 [공부노트]

# 출처: https://suri78.tistory.com/128 [공부노트]