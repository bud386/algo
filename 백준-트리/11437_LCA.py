import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0] * (N+1)
visited = [0] * (N+1)
def depth_cnt(node, d):
    visited[node] = 1
    depth[node] = d
    for n_node in graph[node]:
        if visited[n_node] == 0:
            depth_cnt(n_node, d+1)
depth_cnt(1, 1)



# 부모노드와 깊이 확인
def dfs(node, arr):
    arr.append([node, depth[node]])
    for n_node in graph[node]:
        if depth[n_node] < depth[node]:
            dfs(n_node, arr)
            return

def dfs(node, arr):
    if depth[node] == depth[shallow_node]:
        return node
    for n_node in graph[node]:
        if depth[n_node] < depth[node]:
            dfs(n_node, arr)
            return



def bfs():
    while a_que:
        a_node = a_que.popleft()
        if depth[a_node] == depth[b_node]:
            break
        for n_a in graph[a_node]:
            if depth[n_a] < depth[a_node]:
                a_que.append(n_a)
                break

    while a_que and b_que:
        a_node = a_que.popleft()
        b_node = b_que.popleft()
        for n_a in graph[a_node]:
            if depth[n_a] < depth[a_node]:
                a_que.append(n_a)
                break
        for n_b in graph[b_que]:
            if depth[n_b] < depth[b_node]:
                b_que.append(n_b)
                break

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    min_depth = min(depth[a], depth[b])
    a_depth = depth[a]
    b_depth = depth[b]
    a_que = deque()
    b_que = deque()
    a_que.append(a)
    b_que.append(b)
    bfs()
    # a_parents = []
    # b_parents = []    
    # dfs(a, a_parents)
    # dfs(b, b_parents)

    # # print(a_parents)
    # # print(b_parents)
    # if a_depth < b_depth:
    #     for i in range(a_depth+1):
    #         if a_parents[i][0] == b_parents[b_depth-a_depth+i][0] and a_parents[i][1] == b_parents[b_depth-a_depth+i][1]:
    #             print(a_parents[i][0])
    #             break
    # else:
    #     for i in range(b_depth+1):
    #         if b_parents[i][0] == a_parents[a_depth-b_depth+i][0] and b_parents[i][1] == a_parents[a_depth-b_depth+i][1]:
    #             print(b_parents[i][0])
    #             break

