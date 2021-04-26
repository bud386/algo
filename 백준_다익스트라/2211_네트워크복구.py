import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize 

N, M = map(int, input().split())    # 컴퓨터 수, 회선 수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split()) # 컴퓨터, 연결 컴퓨터, 통신시간
    graph[A].append((C, B))
    graph[B].append((C, A))

q= [[0, 1]] # 1번 컴퓨터 부터 시작
distance = [inf] * (N+1)    # 최단 통신 시간
distance[1] = 0

recovered = [[] for _ in range(N+1)]    # 각 컴퓨터별로 복구한 회선저장할 리스트
asd = 0
while q:
    asd += 1
    print(asd, '?')
    w, computer = heappop(q)
    if distance[computer] < w:
        continue
    for weight, connected_computer in graph[computer]:
        total_weight = w + weight
        if distance[connected_computer] > total_weight:
            distance[connected_computer] = total_weight
            heappush(q, [total_weight, connected_computer])
            
            for i in range(N+1):
                if connected_computer in recovered[i]:  # 복구할 컴퓨터가 앞에서 복구된적이 있다면
                    recovered[i].remove(connected_computer) # 해당 복구회선 지우기.
            recovered[computer].append(connected_computer)  # computer별로 복구회선 추가


cnt = 0    
for i in range(N+1):
    if distance[i] != inf:
        cnt += 1
print(cnt-1)    # 1번 컴퓨터 제외하고 cnt

for i in range(N+1):
    if recovered[i]:    # i번째 컴퓨터에 복구된 회선이 있다면
        for j in range(len(recovered[i])):
            print(i, recovered[i][j])   # i와 i와 연결된 모든 복구된 회선 출력

