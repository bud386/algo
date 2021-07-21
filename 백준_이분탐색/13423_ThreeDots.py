import sys
input = sys.stdin.readline

for tc in range(int(input())):
    N = int(input())
    nums = sorted(list(map(int, input().split())))
    max_gap = (nums[-1] - nums[0]) // 2
    cnt = 0 
    
    # 왼쪽 점, 중간 점 구하기
    for i in range(N):
        for j in range(i+1, N):
            gap = nums[j] - nums[i]
            
            if gap > max_gap:
                break # 최대 gap 보다 크면 다음 왼쪽 점으로 이동
            
            r_num = nums[j] + gap   # 오른쪽 점
            start = j+1
            end = N-1
            while start <= end:
                if nums[start] == r_num:
                    cnt += 1
                    break
                if nums[end] == r_num:
                    cnt += 1
                    break

                mid = (start + end) // 2
                if r_num < nums[mid]:
                    end = mid - 1
                elif r_num > nums[mid]:
                    start = mid + 1
                else:
                    cnt += 1
                    break


    print(cnt)