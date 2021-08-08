import sys 
input = sys.stdin.readline
from collections import defaultdict

T = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


a_sum = defaultdict(int)
b_sum = defaultdict(int)

for i in range(n):
    cumulative_sum = a[i]        
    a_sum[cumulative_sum] += 1    
    for j in range(i+1, n):        
        cumulative_sum += a[j]    
        a_sum[cumulative_sum] += 1        

ans = 0    
for i in range(m):            
    for j in range(i, m):        
        cumulative_sum = sum(b[i:j+1]) 
        ans += a_sum[T - cumulative_sum]


      # print(j+1, 'j')
        # for a_key, a_value in a_sum.items():
        #     if a_key + cumulative_sum == T:
        #         # print(a_key, a_value)
        #         ans += a_value
        
# for a_key, a_value in a_sum.items():
#     for b_key, b_value in b_sum.items():
#         if a_key + b_key == T:
#             ans += (a_value * b_value)

print(ans)
        

        