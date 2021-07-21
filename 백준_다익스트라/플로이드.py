import sys
input = sys.stdin.readline
inf = sys.maxsize 

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
dist = [[inf] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            dist[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    dist[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1): # 중간노드
    for a in range(1, n + 1):   # 시작노드
        for b in range(1, n + 1): # 도착노드
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b]) # 시작 -> 종료 vs 시작 -> 중간 -> 종료
            