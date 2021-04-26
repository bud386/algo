import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize 

N, M = map(int, input().split())  # 지점의 수, 도로의 수
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append([t, b])
    graph[b].append([t, a])

if len(graph[N]) == 1:
    print(-1)
else:
    q = []
    distance = [inf] * (N+1)  
    distance[s] = 0    
    heappush(q, [N, 0])    

    while q:
        node, weight = heappop(q)   
        for n_node, n_weight in graph[node]:
            total_weight = weight + n_weight
            if distance[n_node] > total_weight:    
                distance[n_node] = total_weight    
                heappush(q, [n_node, total_weight]) 




import sys, heapq

input = sys.stdin.readline

def djt(s, e):
    time = [MAX_TIME for _ in range(n+1)]
    time[1] = 0
    heap = [(0, 1)]
    while heap:
        t, now = heapq.heappop(heap)
        if now==n: break
        for next, plus in graph[now]:
            if s==now and e==next or s==next and e==now: continue
            if t+plus < time[next]:
                time[next] = t+plus
                if not s: pre[next] = now
                heapq.heappush(heap, (time[next], next))
    return time[n]

MAX_TIME = 10000000
        
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
