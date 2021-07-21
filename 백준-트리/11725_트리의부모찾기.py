import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)


visited = [0]*(N+1)

def dfs(node):
    for i in tree[node]:
        if visited[i] == 0:
            visited[i] = node
            # print('부모:',node, '자식:', i)
            dfs(i)


dfs(1)
for i in range(2, N+1):
    print(visited[i])