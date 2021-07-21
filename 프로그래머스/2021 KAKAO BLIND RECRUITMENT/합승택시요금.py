from heapq import heappush, heappop


def solution(n, s, a, b, fares): # 지점수, 출발지, a집, b집,
    print('?')
    graph = [[] for _ in range(n+1)]
    for fare in fares: 
        u, v, w = fare    # 시작, 끝, 요금
        graph[u].append((v,w))
        graph[v].append((u,w))
    
    print('??')
    dist = dijkstra(graph, n, s) # start에서 각 지점까지의 최소 비용
    answer = dist[a] + dist[b] #1. start-> a + start -> b
    print(dist)
    
    # new_dist = dijkstra(graph, n, a) # a집으로 부터 각 지점까지의 최소 비용
    # answer = min(answer, dist[a] + new_dist[b]) #2. start -> a -> b (=start -> b -> a)
    
    print(new_dist)
    #3 start -> 중간지점(i) -> a, b
    for i in range(1, n+1):
        new_dist = dijkstra(graph, n, i) # 중간 지점부터 각 지점까지의 최소 비용
        answer = min(answer, dist[i] + new_dist[a] + new_dist[b])
    print(answer)
    return answer

def dijkstra(graph, n, s):
    inf = 99999999
    q = []
    distance = [inf] * (n+1)   # 시작 노드로부터 모든 노드 까지의 최소 비용을 담을 리스트
    distance[s] = 0    # 시작점에서 시작점 까지의 비용 항상 0
    heappush(q, [s, 0])    # q에 시작노드, 비용 push

    while q:
        node, weight = heappop(q)   
        for n_node, n_weight in graph[node]:
            total_weight = weight + n_weight
            if distance[n_node] > total_weight:    # 현재 비용보다 싸면
                distance[n_node] = total_weight    # 최소 비용 갱신
                heappush(q, [n_node, total_weight]) # q에 노드와 해당 노드까지의 비용 push
                    
    return distance

fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]	
solution(6, 4, 6, 2, fares)


#########################
# 학일님 풀이
def solution(n, s, a, b, fares):
    MAX = 20000001
    tree = [[MAX]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        tree[i][i] = 0

    for aa, bb, c in fares:
        tree[aa][bb] = c
        tree[bb][aa] = c

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                sum = tree[i][k] + tree[k][j]
                if tree[i][j] > sum:
                    tree[i][j] = sum
                tree[j][i] = tree[i][j]
    answer = MAX
    for i in range(1, n+1):
        sum = tree[s][i]+tree[i][a]+tree[i][b]
        if answer > sum:
            answer = sum
    return answer