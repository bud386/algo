import sys 
input = sys.stdin.readline
inf = sys.maxsize
N = int(input())
nums = list(map(int, input().split()))

left = 0
right = N-1

ans = inf
while left < right:
    total = nums[left]+nums[right]
    if total == 0:
        l_ans = left
        r_ans = right
        break
    if ans > abs(total):
        ans = abs(total)
        l_ans = left
        r_ans = right    

    if total > 0:
        right -= 1
    else:
        left += 1

print(nums[l_ans], nums[r_ans])