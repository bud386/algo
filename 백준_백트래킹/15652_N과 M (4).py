import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pick = []
def back_track(N, M, start):
    if len(pick) == M:
        print(*pick)
        return
        
    for i in range(start, N+1):
        pick.append(i)
        back_track(N, M, i)
        pick.pop()

back_track(N, M, 1)