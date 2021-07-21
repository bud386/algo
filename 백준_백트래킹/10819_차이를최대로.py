import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

visited = [0] * N # 해당 인덱스에 방문했는지 체크할 배열
new_num = [0] * N # 순열을 저장할 새로운 배열
ans = 0

def permutation(idx):    
    global ans  
    if idx == N:
        cal = 0
        for i in range(N-1):
            cal += abs(new_num[i] - new_num[i+1])        
        if cal > ans:
            ans = cal        
        return
        
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            new_num[idx] = num[i]            
            permutation(idx + 1)
            visited[i] = 0            

permutation(0)
print(ans)