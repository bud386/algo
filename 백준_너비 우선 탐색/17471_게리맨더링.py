import sys
input = sys.stdin.readline

N = int(input())    # 도시 개수
population = [0] + list(map(int, input().split())) # 각 도시의 인구
graph = [[] for _ in range(N+1)] # 연결된 도시
for i in range(1, N+1):
    connected = list(map(int, input().split()))
    graph[i] = connected[1:]

nums = [i for i in range(1, N+1)]   #
A = [] # A구역에 속한 도시
ans = 9999999

def dfs(node, visited, partition, part):        
    for n_node in graph[node]:
        if partition[n_node] == part and visited[n_node] == 0:
            visited[n_node] = 1
            dfs(n_node, visited, partition, part)


def combi(s, k):
    global ans
    if len(A) == k: # A 영역에 k개의 도시를 선택했을때 
        # A에는 a파트 도시번호, B에는 b파트 번호
        B = [city for city in nums if city not in A]        

        A_population = 0 # A 구역 인구 합
        B_population = 0 # B 구역 인구 합
        partition = [0] * (N+1) # 각 도시가 A 구역인지, B 구역인지  
        for a in A:
            partition[a] = 'a'
            A_population += population[a]
        for b in B:
            partition[b] = 'b'
            B_population += population[b]

        visited = [0] * (N+1)
        visited[A[0]] = 1
        visited[B[0]] = 1
        dfs(A[0], visited, partition, 'a')
        dfs(B[0], visited, partition, 'b')     
        if sum(visited) == N:
            ans = min(ans, abs(A_population - B_population))            
        return
    
    # 조합 뽑기
    for i in range(s, N):
        A.append(nums[i])
        combi(i+1, k)
        A.pop()

for k in range(1, N//2+1): # N에서 k개 뽑기
    combi(0, k)

if ans == 9999999:
    print(-1)
else:
    print(ans)


