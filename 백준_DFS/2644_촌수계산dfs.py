import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)

print(graph)
def dfs(s, e, cnt):
    visited[s] = 1
    for i in graph[s]:
        if i == e:
            print('정답', cnt)
            # print(cnt)
        if visited[i] == 0:
            print('친척:',i, '촌수:', cnt)
            dfs(i, e, cnt+1)
    
dfs(a, b, 1)

if visited[b] == 0:
    print(-1)













# N = int(input())
# a,b = map(int,input().split())
# M = int(input())

# parent = [i for i in range(N+1)]

# for _ in range(M):
#     x,y = map(int,input().split())
#     parent[y] = x

# def find(x,lst):
#     lst.append(x)
#     if parent[x] == x:
#         return lst
#     else:
#         return find(parent[x],lst)
# a_lst = find(a,[])
# b_lst = find(b,[])
# ans = -1
# for idx, var in enumerate(b_lst):
#     if var in a_lst:
#         ans = idx+a_lst.index(var)
#         break
# print(ans)