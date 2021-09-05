import sys
input = sys.stdin.readline

words = input().strip()
bomb = list(input().strip())
n = len(bomb)
new = []

for i in words:
    new.append(i)    
    if len(new) >= n:   # 폭탄길이보다 길고
        if new[-1] == bomb[-1]: # 마지막 단어가 폭탄의 마지막이랑 같고            
            if new[-n:] == bomb:    # 뒤에서 부터 폭탄의 길이            
                new = new[0:-n]
                

if new:
    print(''.join(new))
else:
    print('FRULA')

# while True:
#     flag = False
#     new = temp
#     temp = []    
#     i, j = 0, 0
#     k = len(new)
#     while i < k:
#         temp.append(new[i])            
#         if new[i] == bomb[j]:
#             j += 1
#             if j == n:
#                 flag = True                
#                 for _ in range(n):
#                     temp.pop()
#                 j = 0
#         else:        
#             j = 0
#             if new[i] == bomb[j]:
#                 j += 1                
#         i+= 1    
#     if flag == False:
#         break