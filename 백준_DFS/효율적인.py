import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    
# print(graph)
q = deque()
cnt_node = []
visited = [0] * (N+1)

leaf_visited = []

# 1. 리프노드에 대한 탐색
for leaf_node in range(1, len(graph)):
    if graph[leaf_node] == []:
        visited = [0] * (N+1)
        q.append(leaf_node)
        visited[leaf_node] = 1
        leaf_visited.append(leaf_node)
        cnt = 0
        while q:
            now = q.pop()
            # 부모 노드 탐색해서 q에 넣어줌
            for p_node in range(1, len(graph)):
                if now in graph[p_node] and visited[p_node] == 0:
                    visited[p_node] = 1
                    q.append(p_node)
                    cnt += 1
                    leaf_visited.append(p_node)
        cnt_node.append([cnt, leaf_node])

for node in leaf_visited:
    visited[node] = 1
visited[0] = 1


# 2. 사이클이 있는 노드에 대한 탐색
cycle_list = []
cycle_cnt = []
while 0 in visited:
    q.append(visited.index(0))
    cycle = [visited.index(0)]
    visited[visited.index(0)] = 1
    
    while q:
        now = q.pop()
        # 부모 노드 탐색해서 q에 넣어줌
        for p_node in range(1, len(graph)):
            if now in graph[p_node] and visited[p_node] == 0:
                visited[p_node] = 1
                q.append(p_node)
                cycle.append(p_node)
    cycle_list.append(cycle)
    cycle_cnt.append(len(cycle))

if cycle_cnt:
    max_cycle_cnt = max(cycle_cnt)
else:
    max_cycle_cnt = 0
# print(leaf_visited)
ans = []
# 리프 노드가 있어서 cnt_node에 추가되어 있다면
if cnt_node:
    # print(cnt_node)
    # print(cycle_list)
    max_leaf_cnt = max(cnt_node)[0]
    if max_leaf_cnt > max_cycle_cnt:
        for i in cnt_node:
            if i[0] == max_leaf_cnt:
                ans.append(i[1])
    
    elif max_leaf_cnt == max_cycle_cnt:
        for i in cnt_node:
            if i[0] == max_leaf_cnt:
                ans.append(i[1])
        for cycle in cycle_list:
            if len(cycle) == max_cycle_cnt:
                for n in cycle:
                    ans.append(n)
    else:
        for cycle in cycle_list:
            if len(cycle) == max_cycle_cnt:
                for n in cycle:
                    ans.append(n)
else:
    for cycle in cycle_list:
        if len(cycle) == max_cycle_cnt:
            for n in cycle:
                ans.append(n)


        
print(*sorted(ans))



# 12 11
# 2 1
# 3 2
# 4 2
# 5 1
# 2 5
# 6 7
# 7 8
# 8 9
# 9 10
# 10 11
# 11 12

# 11 10
# 1 2
# 2 3
# 3 1
# 4 5
# 5 6
# 6 4
# 7 8
# 7 10
# 8 9
# 9 11