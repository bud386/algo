import sys
input = sys.stdin.readline

N = int(input())
values = sorted(list(map(int, input().split())))

start = 0
end = N-1
left = 0
right = N - 1

ans = abs(values[0] + values[N-1]) 

while start < end:
    temp = values[start] + values[end]
    
    if abs(temp) < ans:
        ans = abs(temp)
        left = start
        right = end
        if ans == 0:
            break
    
    if temp > 0:
        end -= 1
    else:
        start += 1         
        
print(values[left], values[right])