import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
M_list = sorted(list(map(int, input().split())))
animals = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b in animals:        
    start = 0
    end = M-1 
    while start <= end:
        mid = (start+end) // 2  
        dist = abs(M_list[mid]-a) + b        

        if dist <= L:
            ans += 1
            break
        else:
            if M_list[mid] < a:                
                start = mid + 1
            else: 
                end = mid - 1

print(ans)