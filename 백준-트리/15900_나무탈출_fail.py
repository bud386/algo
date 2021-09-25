import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
leaf_cnt = 0

# def dfs(node):
#     global leaf_cnt
#     visited[node] = 1
#     leaf = True
#     for n_node in tree[node]:
#         if visited[n_node] == 0:
#             visited[n_node] = 1
#             leaf = False
#             dfs(n_node)
#     if leaf:
#         leaf_cnt += 1

for i in range(2, N+1):
    if len(tree[i]) == 1:
        leaf_cnt += 1

# dfs(1)
middle_node = N-1-leaf_cnt
if middle_node % 2:
    print('No')
else:
    print("Yes")