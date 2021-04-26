import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

N = int(input())    # 도시의 개수
M = int(input())    # 버스의 개수
graph = [[] for _ in range(N+1)]
for _ in range(M): 
    u, v, w = map(int, input().split())    # 시작, 끝, 요금
    graph[u].append((v,w))
s, e = map(int, input().split())    # 시작점, 도착점

q = []
distance = [inf] * (N+1)   # 시작 노드로부터 모든 노드 까지의 최단 거리를 담을 리스트
distance[s] = 0    # 시작점에서 시작점 까지의 거리는 항상 0
heappush(q, [s, 0])    # q에 시작노드, 거리push

while q:
    node, weight = heappop(q)   
    for n_node, n_weight in graph[node]:
        total_weight = weight + n_weight
        if distance[n_node] > total_weight:    # 현재 거리보다 짧으면
            distance[n_node] = total_weight    # 최단 거리 갱신
            heappush(q, [n_node, total_weight]) # q에 노드와 해당 노드까지의 거리 push
            
        # if distance[n_node] > weight + n_weight:    # 현재 거리보다 짧으면
        #     distance[n_node] = weight + n_weight    # 최단 거리 갱신
        #     heappush(q, [n_node, distance[n_node]]) # q에 노드와 해당 노드까지의 거리 push

print(distance[e])

