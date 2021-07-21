import sys
input = sys.stdin.readline
from collections import deque

def D(n):
    n *= 2
    if n > 9999:
        n %= 10000
    return n

def S(n):
    if n == 0:
        return 9999
    else:
        return n-1

def L(n):
    d1 = n % 10 # 1의 자리
    d2 = (n % 100) // 10 # 10의 자리
    d3 = (n % 1000) // 100 # 100의 자리
    d4 = (n % 10000) // 1000 # 1000의 자리
    n = d4 + d1*10 + d2*100 + d3*1000
    return n

def R(n):
    d1 = n % 10 # 1의 자리
    d2 = (n % 100) // 10 # 10의 자리
    d3 = (n % 1000) // 100 # 100의 자리
    d4 = (n % 10000) // 1000 # 1000의 자리
    n = d2 + d3*10 + d4*100 + d1*1000
    return n
    
calculate = ['D', 'S', 'L', 'R']

for _ in range(int(input())):
    a, b = map(int, input().split())    
    q = deque()
    q.append([a, ''])
    visited = [0] * 10000
    visited[a] = 1    

    while q:
        now, ans = q.popleft()        
        if now == b:
            print(ans)
            break
        for i in range(4):
            if i == 0:
                next = D(now)
            elif i == 1:
                next = S(now)
            elif i == 2:
                next = L(now)
            else:
                next = R(now)
            if visited[next] == 0:
                visited[next] = 1
                q.append([next, ans+calculate[i]])            


                