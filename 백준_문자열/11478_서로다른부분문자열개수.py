import sys
input = sys.stdin.readline

S = input().strip() 
n = len(S)  
ans = []

for i in range(1, n+1): 
    for j in range(n+1-i): 
        ans.append(S[j:j+i])

print(len(set(ans)))