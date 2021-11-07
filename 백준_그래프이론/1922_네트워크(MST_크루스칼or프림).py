import sys
input = sys.stdin.readline

# 1. 크루스칼
N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find(node):
    if node != parent[node]:
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    print(parent)
    if a_root < b_root:
        parent[a_root] = b_root
    else:
        parent[b_root] = a_root

edges = []
for _ in range(M):
    edges.append(list(map(int, input().split())))
edges.sort(key= lambda x: x[2])
print(edges, 'asdasd')

ans = 0
visited = 0 
for edge in edges:
    if visited == N-1:
        break
    a, b, cost = edge
    if find(a) != find(b):
        union(a, b)
        ans += cost
        visited += 1

print(ans)

# 2. 프림
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])
    graph[b].append([cost, a])

q = []
visited = [0] * (N+1)
for connected in graph[1]:
    heapq.heappush(q, connected)
visited[1] = 1

ans = 0
while q:
    cost, node = heapq.heappop(q)
    if visited[node] == 0:
        visited[node] = 1
        ans += cost    
        for connected in graph[node]:
            heapq.heappush(q, connected)
    if sum(visited) == N:
        break

print(ans)