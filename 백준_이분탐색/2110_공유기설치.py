# import sys
# input = sys.stdin.readline

# N, C = map(int, input().split())
# x = [int(input()) for _ in range(N)]
# x.sort()
# l = 0
# r = N-1
# cnt = 2
# gap = x[r]-x[l]
# while cnt <= C:
#    for i in range(l+1, r):
#        if 
#     cnt += 1
# print(x_list)
# print(x_list[r]-x_list[l], '?')


n, c = map(int, input().split())
 
arr = [int(input()) for _ in range(n)]
arr.sort()
 
low = 1 # 최소거리
high = arr[-1] - arr[0] # 최대 거리
result = 0
 
while(low <= high):
    mid = (low + high) // 2 # mid는 gap
    
    value = arr[0]  # 시작점
    count = 1 # 설치중인 공유기 개수
    #집 위치가 거리보다 멀거나 같으면 공유기 설치
    for i in range(1, n):
        if arr[i] >= value + mid:   # 집의 위치 >= 이전집위치 + 거리보다 크거나 같다면
            # print(value, arr[i], mid, count, result) 
            value = arr[i]  # 공유기 설치
            count += 1
    if count >= c: # c개 이상의 공유기를 설치할 수 있는 경우 정답 가능
        low = mid + 1
        result = mid
    else: # c개 이상의 공유기를 설치할 수 없는 경우
        high = mid - 1
        
print(result)