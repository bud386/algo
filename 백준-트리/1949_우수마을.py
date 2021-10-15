import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n = int(input())
populations = [0]
populations+= list(map(int, input().split()))

visited = [0] * (n+1)
dp = [[0, 0] for _ in range(n + 1)]

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(city):
    visited[city] = 1
    dp[city][0] = populations[city]
    for n_city in graph[city]:
        if not visited[n_city]:
            dfs(n_city)
            dp[city][0] += dp[n_city][1] # 이전 마을을 우수마을로 지정 (인접마을은 우수마을 안됨)
            dp[city][1] += max(dp[n_city][0], dp[n_city][1]) # 이전 마을 우수마을 지정 x (인접마을은 우수마을이어도 되고 아니어도 됨)
dfs(1)
print(max(dp[1][0], dp[1][1]))