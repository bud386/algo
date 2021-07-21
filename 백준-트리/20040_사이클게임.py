import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
# graph = [[] for _ in range(n+1)]
parents = [i for i in range(n)]

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):
    global cycle, cnt
    x = find(x)
    y = find(y)
    if x == y:
        cycle = True
        # cnt += 1
        return
    if x > y:
        parents[x] = y
    else:
        parents[y] = x

cycle  = False 
ans = 0
# cnt = 0 # 처음 사이클을 기록
for i in range(1, m+1):
    u, v = map(int, input().split())
    if cycle == False:
        union(u, v)        
    if cycle == True and ans == 0:        
        ans = i

print(ans)