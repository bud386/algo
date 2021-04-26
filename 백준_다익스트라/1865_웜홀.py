import sys
input = sys.stdin.readline
inf = sys.maxsize 

def bellman_ford(s, graph):
    ans = 'NO'  # 음수 사이클이 있는지 표시

    for _ in range(N-1):   
        for i in range(2*M+W):    # 도로의수 + 웜홀의 수
            s, e, t = graph[i]    
            if distance[e] > distance[s] + t:  
                distance[e] = distance[s] + t
                # print('dist', distance)

    # 음의 사이클이 존재하는지 검증
    for i in range(2*M+W):
        s, e, t = graph[i]    
        if distance[e] > distance[s] + t: 
            ans = 'YES'
            break
    
    return ans
    

for tc in range(int(input())):
    N, M, W = map(int, input().split())
    graph = []
    for _ in range(M):
        s, e, t = map(int, input().split())
        graph.append([s, e, t])
        graph.append([e, s, t])

    for _ in range(W):
        s, e, t = map(int, input().split())
        graph.append([s, e, -t])

    distance = [inf] * (N+1)
    # 음의 사이클만 있느지 확인하면 되기 때문에 시작점은 상관없다
    distance[1] = 0

    print(bellman_ford(1, graph))

