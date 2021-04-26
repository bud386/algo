import sys
input = sys.stdin.readline 
# def connect(k):    
#     global cnt, pick
#     # print(k)
#     if pick == N:
#         cnt += 1
#         # print(cnt)
#         return
#     for i in range(k, M):
#         pick += 1
#         connect(i+1)
#         pick -= 1

def fact(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

for tc in range(int(input())):
    N, M = map(int, input().split())
    # cnt = 0
    # pick = 0
    # connect(0)
    # print(cnt)
    cnt = fact(M) // (fact(N) * fact(M-N))
    print(cnt)
