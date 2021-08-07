import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
# dp = [1] * N
# ans = 1
# for i in range(N):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
#             if ans < dp[i]:
#                 ans = dp[i]
# print(ans)



# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4#s-3.2
def binary_search(start, end, num):
    while start < end:
        mid =(start + end) // 2

        if cnt[mid] > num:
            end = mid
        else:
            start = mid + 1
            
    return end


cnt = []    # index는 수열의 길이, 값은 해당 수열의 마지막 값
for i in range(N):
    if len(cnt) == 0:
        cnt.append(nums[i])
    else:
        if cnt[-1] < nums[i]:
            cnt.append(nums[i])
        else:
            idx = binary_search(0, len(cnt), nums[i])
            cnt[idx] = nums[i]

print(len(cnt))




#######################################################
# 스터디
import sys
input = sys.stdin.readline


n = int(input())
number = list(map(int, input().split()))

st = [number[0]]

for num in number[1:]:

    if st[-1] > num:

        l, r = 0, len(st)-1

        while l <= r:
            mid = (l+r)//2
            if st[mid] < num: l = mid + 1
            else: r = mid - 1

        st[l] = num

    elif st[-1] < num: st.append(num)
    
print(len(st))


