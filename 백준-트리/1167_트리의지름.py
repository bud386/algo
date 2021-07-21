import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N):
    info = list(map(int, input().split()))
    p = info[0]    
    for i in range(1, len(info), 2):
        if info[i] == -1:
            break
        graph[p].append((info[i], info[i+1]))
        

def dfs(node, distance):
    global max_dist, max_node
    visited[node] = 1            
    for v, w in graph[node]:
        if visited[v] == 0:
            dist = distance + w
            # print(dist)      
            if max_dist < dist:
                max_dist = dist      
                max_node = v
            dfs(v, dist)

visited = [0] * (N+1)   
max_dist, max_node = 0, 0
dfs(1, 0)
visited = [0] * (N+1)   
dfs(max_node, 0)

print(max_dist)

