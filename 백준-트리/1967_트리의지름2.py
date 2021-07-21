import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c, w = map(int, input().split())
    graph[p].append((c, w))
    graph[c].append((p, w))
        

def dfs(node, distance):
    global max_dist, max_node
    visited[node] = 1            
    for v, w in graph[node]:
        if visited[v] == 0:
            dist = distance + w
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








## 트리 bfs



print()
from sys import stdin
from collections import deque
input = stdin.readline

def find_tree(x):
    
    flag = True
    q=deque()
    q.append(x)

    while q:
        print(q)
        now = q.popleft()
        if visited[now]:
            print(now)
            flag = False # 네트워크 안에 들어있는게 모두 방문되어야함.
        visited[now] = True

        for next in tree[now]:
            print(now, next, visited, '#########')
            if not visited[next]:
                print(now, next, visited, '????')  
                q.append(next)
                
    return flag

count = 0

while True:
    count +=1
    n,m = map(int,input().split())
    if n==0 and m == 0: break

    tree = [ [] for _ in range(n+1)]
    visited = [False]*(n+1)

    for i in range(m):
        a,b=map(int,input().split())
        if a==b: continue
        tree[a].append(b)
        tree[b].append(a)

    result = 0
    print(tree)
    for i in range(1,n+1):
        if visited[i]:
            continue
        if find_tree(i):
            result += 1

    if result == 0:
        print("Case {}: No trees.".format(count))
    elif result == 1:
        print("Case {}: There is one tree.".format(count))
    else:
        print("Case {}: A forest of {} trees.".format(count,result))

