import sys
input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())
n = len(S)

while n < len(T):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[-1:-len(T)-1:-1]
if S == T:
    print(1)
else:
    print(0)


# def sol(word):    
#     if len(word) == n:
#         if word == T:
#             print(1)
#             exit()
#         return        
#     word.append('A')        
#     sol(word)
#     word.pop()
#     word = word[-1:-len(word)-1:-1] + ['B']
#     sol(word)

# sol(S)
# print(0)


