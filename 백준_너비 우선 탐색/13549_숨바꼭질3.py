# 다익스트라 이용
import sys
input = sys.stdin.readline
from heapq import heappop, heappush
inf = sys.maxsize

# 수빈 N, 동생 K
N, K = map(int, input().split()) 
move = [2, 1, -1]

q = []
heappush(q, [0, N]) # 총 걸린 시간, 시작 지점
visited = [inf]* (100001)
visited[N] = 0

while q:
    time, now = heappop(q)
    for i in range(3):
        if i == 0:
            next = now * 2            
            total_time = time    
        else:
            next = now + move[i]                
            total_time = time + 1        
        if 0 <= next <= 100000:
            if visited[next] > total_time:
                visited[next] = total_time
                heappush(q, [total_time, next])

print(visited[K])