### 스터디 코드
import sys, heapq

sys.setrecursionlimit(100000000)

input = sys.stdin.readline

n, m = map(int, input().split())

bridge = [dict() for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    if b in bridge[a]:
        if bridge[a][b] < c:
            bridge[a][b] = c
            bridge[b][a] = c
    else:
        bridge[a][b] = c
        bridge[b][a] = c

start, end = map(int, input().split())
visit = [0]*(n+1)

que = []

heapq.heappush(que, (-1000000000, start))

while que:

    cost, idx = heapq.heappop(que)
    
    if visit[idx]: continue
    visit[idx] = 1
    
    if idx==end:
        break

    for i, c in bridge[idx].items():
        heapq.heappush(que, (max(cost, -c), i))

print(-cost)
##############################################################################


import heapq
import sys
input = sys.stdin.readline
from heapq import heappush, heappop
inf = sys.maxsize

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)  # 최대힙
        dist = -1 * dist        
        if now == end:
            print(dist)
            break

        if max_limit[now] > dist: # 이미 최대 중량인경우
            continue

        for i in graph[now]: # 정렬된 상태이므로 높은 중량부터 탐색이 됨.
            if dist == 0: # dist가 0인게 문제여...
                max_limit[i[1]] = i[0]
                heapq.heappush(q, (-max_limit[i[1]], i[1]))
            # 기존에 저장된 값이 dist(이전 도시에서의 최대중량)와 현재 다리 최대 중량 보다 작다면...
            # 이렇게 한 이유는 다리가 중복 연결되어있는 가능성이 있기 때문
            elif max_limit[i[1]] < i[0] and max_limit[i[1]] < dist:  # 다음 도시까지 최대중량이 지금 다리보다 작을때, 
                max_limit[i[1]] = min(dist, i[0]) # ✅ 이전도시 최대 중량과 현재 다리 최대 중량 중 작은 값을 저장
                heapq.heappush(q, (-max_limit[i[1]], i[1]))

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([C, B])
    graph[B].append([C, A])

a, b = map(int, input().split())
q = []
heappush(q, [0, a])
# ans = inf
max_limit = [0] * (N+1)
# visited = [[0]*(N+1) for _ in range(N+1)]
# for limit, city in graph[a]:
#     max_limit[city] = limit
#     visited[a][city] = limit
#     visited[city][a] = limit
#     heappush(q, [-limit, city])
# ans = inf

dijkstra(a, b)

# 현재 이어진 다리중 가장 중량이 큰것부터 확인
# while q:
#     limit, city = heappop(q)
#     limit *= -1
#     # print(city, limit, '?')    
#     ans = min(ans, limit)
#     if city == b:
#         print(ans)
#         break
#     if max_limit[city] > limit: # 이미 최대 중량인 경우
#         continue

#     for n_limit, n_city in graph[city]:        
#         if max_limit[n_city] < n_limit: # 다음 방문할 도시까지 다리 중량이 지금까지 기록된거보다 클때
#             if max_limit[n_city] < limit:        
#                 max_limit[n_city] = min(limit, n_limit) # n_city까지의 경로중 가장 작은걸 저장
#                 heappush(q, [-max_limit[n_city], n_city])
#             # if visited[city][n_city] == 0:  # city -> n_city 다리를 건넌적이 없다면
#             #     visited[city][n_city] = n_limit
#             #     visited[n_city][city] = n_limit
#             #     max_limit[n_city] = min(limit, n_limit) # n_city까지의 경로중 가장 작은걸 저장
#             #     heappush(q, [-n_limit, n_city])
#             # else:
#             #     if n_limit > visited[city][n_city]: # city -> n_city 다리를 건넌적이 있어도 더 중량 한계가 큰 도시가 잇을때(두 도시에는 여러 다리가 있을수 있다.)
#             #         visited[city][n_city] = n_limit
#             #         visited[n_city][city] = n_limit
#             #         max_limit[n_city] = min(limit, n_limit) # n_city까지의 경로중 가장 작은걸 저장
#             #         heappush(q, [-n_limit, n_city])

    






# import heapq
# import sys

# input = sys.stdin.readline

# def dijkstra(start, end):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     while queue:
#         dist, now = heapq.heappop(queue)  # 최대힙
#         dist = -1 * dist
#         print(dist, now)
#         if now == end:
#             print(dist)
#             break

#         if distance[now] > dist: # 이미 최대 중량인경우
#             continue

#         for i in graph[now]: # 정렬된 상태이므로 높은 중량부터 탐색이 됨.
#             if dist == 0: # dist가 0인게 문제여...
#                 distance[i[1]] = i[0]
#                 heapq.heappush(queue, (-distance[i[1]], i[1]))
#             # 기존에 저장된 값이 dist(이전 도시에서의 최대중량)와 현재 다리 최대 중량 보다 작다면...
#             # 이렇게 한 이유는 다리가 중복 연결되어있는 가능성이 있기 때문
#             elif distance[i[1]] < i[0] and distance[i[1]] < dist: 
#                 distance[i[1]] = min(dist, i[0]) # ✅ 이전도시 최대 중량과 현재 다리 최대 중량 중 작은 값을 저장
#                 heapq.heappush(queue, (-distance[i[1]], i[1]))



# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     graph = [[] for _ in range(n + 1)]
#     for _ in range(m):
#         a, b, c = map(int, input().split())
#         graph[a].append((c, b))
#         graph[b].append((c, a))

#     for i in range(1, n + 1):
#         graph[i].sort(reverse=True)

#     distance = [0] * (n + 1)
#     start, end = map(int, input().split())

#     dijkstra(start, end)
