import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

a, b, c = map(int, input().split())
visted =[[0]*(b+1) for _ in range(a+1)]

ans = []

def dfs(A, B, C): # 각 물통에 들어있는 물의 양
    
    if visted[A][B]:    # 물통 a에 A만큼 물이 들어있고, b에는 B만큼의 물이 들어있을때
        return
    visted[A][B] = 1

    if A == 0:  # A의 물통이 비어있을때
        ans.append(C)

    # a -> b
    if A + B > b:
        dfs(A+B -b, b, C)
    else:
        dfs(0, A+B, C)
    # a -> c, A+B <= C이기 때문에
    dfs(0 , B, C+A)

    # b -> a
    if B + A > a:
        dfs(a, B+A -a, C)
    else:
        dfs(B+A, 0, C)
    # b -> c
    dfs(A , 0 , C+B)

    # c -> a
    if C + A > a:
        dfs(a ,B ,C+A -a)
    else:
        dfs(A+C, B, 0)
    # c -> b
    if C + B > b:
        dfs(A, b, C+B - b)
    else:
        dfs(A, B+C, 0)



    # for i in range(3):
    #     for j in range(3):
    #         if i == j:
    #             continue
    #         if ABC[i] + ABC[j] > abc[j]:
    #             ABC[i] = ABC[i] + ABC[j] - abc[j]
    #             ABC[j] = abc[j]
    #             dfs(ABC)
    #         else:
    #             ABC[j] = ABC[i] + ABC[j]
    #             ABC[i] = 0
    #             dfs(ABC)


dfs(0, 0, c)
print(*sorted(ans))



















https://mygumi.tistory.com/228