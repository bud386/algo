import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


early_adopter = []
for i in range(N+1):
    if len(graph[i]) == 1:
        early_adopter.append(graph[i][0])

# print(set(early_adopter))
print(len(set(early_adopter)))

# 지연님 코드
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(n):
    dp[n][0] = 1 # 내가 얼리어답터
    dp[n][1] = 0
    visit[n] = True

    for i in tree[n]:
        if not visit[i]:
            dfs(i)
            dp[n][0] += min(dp[i][0], dp[i][1]) # 자식도 얼리가나 아닐수있음
            dp[n][1] += dp[i][0] # 내가 얼리아니면 무조건 자식은 얼리

N = int(input())
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
visit = [False] * (N+1)

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dfs(1)
print(min(dp[1][0], dp[1][1]))

# 학일님 코드
import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline

def makeIt(parent, child, flag):

    if dp[child][flag] >= 0: return dp[child][flag]

    if flag:
        result = 1
        for i in link[child]:
            if i != parent:
                result += min(makeIt(child, i, 1), makeIt(child, i, 0))
        dp[child][flag] = result
        return result
    
    result = 0
    for i in link[child]:
        if i != parent:
            result += makeIt(child, i, 1)
    dp[child][flag] = result
    return result

n = int(input())
link = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

dp = [[-1]*2 for _ in range(n+1)]
link[0].append(1)
makeIt(0,0,1)
print(min(dp[1][0], dp[1][1]))
