import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = sys.maxsize 

for tc in range(int(input())):
    n, d, c = map(int, input().split()) # 컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호(start)
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split()) # b -> a, 가중치:s
        graph[b].append([s,a])

    distane = [inf] * (n+1)
    distane[c] = 0
    q = [[0, c]] # 시작 weight, 시작점
    

    while q:
        w, computer = heappop(q)
        if distane[computer] < w:
            continue
        for weight, connected_computer in graph[computer]:
            total_weight = w + weight
            if distane[connected_computer] > total_weight:
                distane[connected_computer] = total_weight
                heappush(q, [total_weight, connected_computer])

    cnt = 0
    time = 0
    print(distane)
    for dist in distane:
        if dist != inf: # 최단 거리가 존재할때
            cnt += 1
            time = max(time, dist)  # 최대 거리 time에 저장
    print(cnt, dist)
 