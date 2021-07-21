import sys
input = sys.stdin.readline
inf = sys.maxsize 

N, M = map(int, input().split())
bus = []
for _ in range(M):
    A, B, C = map(int, input().split())
    bus.append([A, B, C])

distance = [inf] * (N+1)
distance[1] = 0
ans = True  # 음수 사이클이 있는지 표시

for _ in range(N-1):    # (정점의 개수-1)번 전체 경로 확인 (모든 정점을 방문하려면 정정의 개수 -1 번 만큼 방문해야한다. )
    for i in range(M):
        s, e, w = bus[i]    # 시작 도시, 도착 도시, 시간 
        if distance[s] != inf and distance[e] > distance[s] + w:    # 음의 간선이 존재하기 때문에 시작점이 아직 inf인지 확인
            distance[e] = distance[s] + w

# 음의 사이클이 존재하는지 검증
for i in range(M):
    s, e, w = bus[i]    
    if distance[s] != inf and distance[e] > distance[s] + w:
        ans = False

if ans:
    for i in range(2, N+1):
        if distance[i] != inf:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)


# if distance[s] != inf 쓰는 이유:
# 이때, 음의 간선이 존재하기 때문에 간선 (s, e)를 볼 때 먼저 dist[s]가 아직 INF인지 확인을 해야 한다.
# 구현에 따라서 둘 다 시작점에서 도달 불가능한 정점 s, e가 존재하고 (s, e) 가중치가 음수일 때(시작점에서 도달할 수 없는 정점들)
# dist[s] = INF, dist[e] = INF-weight 꼴이 나올 수도 있기 때문에.


# **정점의 갯수가 V일 때 V-1번인 이유**
# - https://sodocumentation.net/algorithm/topic/4791/bellman-ford-algorithm












# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# edge = []
# for _ in range(m):
#     edge.append(tuple(map(int, input().split())))

# MAX_TIME = sys.maxsize
# time = [MAX_TIME for _ in range(n+1)]
# time[1] = 0

# def bellman(start):
#     for i in range(n-1):
#         for j in range(m):
#             s, e, t = edge[j]
#             if time[s] != MAX_TIME and time[e] > time[s] + t:
#                 time[e] = time[s] + t

#     for j in range(m):
#         s, e, t = edge[j]
#         if time[s] != MAX_TIME and time[e] > time[s] + t:
#             return True

#     return False

# negativeCycle = bellman(1)

# if negativeCycle: print(-1)
# else :
#     ans = []
#     for i in range(2, n+1):
#         if time[i] == MAX_TIME:
#             ans.append("-1")
#         else:
#             ans.append(str(time[i]))
#     print("\n".join(ans))


