import sys
sys.setrecursionlimit(60000)
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

def match_depth(node):
    if depth[node] == depth[shallow_node]:
        find_ans(node, shallow_node)
        return
    for n_node in graph[node]:
        if depth[n_node] < depth[node]:
            match_depth(n_node)
            break


# 부모노드와 깊이 확인
def find_ans(a, b):
    if a == b:
        print(a)
        return
    for n_node in graph[a]:
        if depth[n_node] < depth[a]:
            n_a = n_node
            break
    for n_node in graph[b]:
        if depth[n_node] < depth[b]:
            n_b = n_node
            break
    find_ans(n_a, n_b)
    
            
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    min_depth = min(depth[a], depth[b])
    a_depth = depth[a]
    b_depth = depth[b]
    if a_depth < b_depth:
        shallow_node = a
        deep_node = b
    else:
        shallow_node = b
        deep_node =  a
    match_depth(deep_node)
    # print(start_node)
    # find_ans(start_node, shallow_node)


