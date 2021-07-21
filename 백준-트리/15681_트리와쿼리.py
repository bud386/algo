import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split()) # 정점의 수, 루트의 번호, 쿼리의 수
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

child_node = [[] for _ in range(N+1)]

# 각 노드별 자식 노드 구하기
def dfs(current_node, parent):
    for node in graph[current_node]:
        if node != parent:
            child_node[current_node].append(node)            
            dfs(node, current_node)

dfs(R, -1)

# 각 노드별 서브트리 카운트
size = [0 for _ in range(N+1)]
def count_subtree(current_node):
    size[current_node] = 1  # 자기 자신 포함
    for node in child_node[current_node]:   # 현재 탐색하는 노드의 자식노드
        count_subtree(node)
        size[current_node] += size[node]

count_subtree(R)

for _ in range(Q):
    print(size[int(input())])
