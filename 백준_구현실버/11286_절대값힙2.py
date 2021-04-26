import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())

que = PriorityQueue()

for _ in range(N):
    num = int(sys.stdin.readline())

    if num:
        que.put((abs(num),num))
    
    else:
        if que.empty():
            print(0)
        else:
            print(que.get()[1])

            
    
# 둘의 차이점은 PriorityQueue가 heappushpop()이나 heapreplace()같이 사용빈도가 낮은 heapq의 메소드들을 가지고있지 않다는 거랑 
# PriorityQueue는 thread-safe인 반면 heapq는 그렇지 않다는 것
# heapq는 느슨한 정렬인 반면, PriorityQueue는 완벽한 정렬을 제공해줍니다.
# queue.PriorityQueue()는 heapq를 기반으로 만들어졌고 thread safe 한 대신 속도가 느리다.