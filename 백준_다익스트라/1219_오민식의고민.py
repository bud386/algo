import sys
input = sys.stdin.readline
inf = -sys.maxsize 

def dfs(end, end_city):

    q = [end]
    visited = [0] * n
    visited[end] = 1
    while q:
        start_node = q.pop()
        for end_node in graph_check[start_node]:
            if visited[end_node] == 0:
                visited[end_node] = 1
                q.append(end_node)

    if visited[end_city] == 1:
        return True
    else:
        return False

def bellman_ford(end_city):
    for _ in range(n-1):    # 전체 경로를 n-1번 확인
        for start, end, cost in graph:    # 시작, 끝, 교통 비용
            if profit[start] != inf and profit[end] < profit[start] + cost + profit_city[end]:  # 경로비용 + 도착도시에서 벌수 있는돈
                profit[end] = profit[start] + cost + profit_city[end]
    
    # 도착 지점을 방문 하지 못한다면 gg 출력
    if profit[end_city] == inf:
        return('gg')

    # 양수 사이클 계산
    for start, end, cost in graph:    # 시작, 끝, 교통 비용
        if profit[start] != inf and profit[end] < profit[start] + cost + profit_city[end]:  
            Gee = dfs(end, end_city)
            if Gee:
                return('Gee')
    
    return profit[end_city]
    

n, start_city, end_city, m = map(int, input().split()) # 도시수, 시작 도시, 도착도시, 교통수단의 개수

graph = []
graph_check = [[] for _ in range(n)] # 양수 사이클 존재할때 dfs로 경로 탐색할 리스트
for _ in range(m):
    s, e, w = map(int, input().split()) # 시작, 끝 ,비용
    graph.append([s, e, -w])
    graph_check[s].append(e)    

profit_city = list(map(int, input().split()))   # 각 도시에서 벌 수 있는 돈

profit = [inf] * n  # 각 도시의 최대 이익 담을 리스트
profit[start_city] = profit_city[start_city] # 시작도시는 방문과 동시에 돈을 번다.

print(bellman_ford(end_city))

