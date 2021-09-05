import sys
input = sys.stdin.readline
inf = sys.maxsize

N = int(input())
nums = sorted(list(map(int, input().split())))

start = 0
end = N-1
center = 1
ans = inf 

for i in range(1, N-1):
    mid = i
    left  = 0
    right = N-1    
    if abs(nums[left] + nums[mid] + nums[right]) < ans:
        ans = abs(nums[left] + nums[mid] + nums[right])
        start = left
        center = mid
        end = right
        if ans == 0:
            break
    
    while left < mid and right > mid:
        temp = nums[left] + nums[mid] + nums[right]

        if abs(temp) < ans:
            ans = abs(temp)
            start = left
            center = mid
            end = right            
            if ans == 0:
                break

        if temp > 0:
            right -= 1
        else:
            left += 1
    

print(nums[start], nums[center], nums[end])