# import sys

# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split()))
# cnt = list(map(int, sys.stdin.readline().split()))

# max_val = -1000000000
# min_val = 1000000000

# print(n,a,cnt)

############################################################################################
N = int(input())
a = list(map(int,input().split()))
cnt = list(map(int,input().split()))
max_ans = -1000000000
min_ans = 1000000000

def dfs(idx, ans):
    global max_ans,min_ans
    
    if idx == N:
        max_ans = max(max_ans, ans)
        min_ans = min(min_ans, ans)
        return
    
    if cnt[0] > 0:
        cnt[0] -= 1
        dfs(idx+1, ans+a[idx])
        # cnt[0] += 1
    if cnt[1] > 0:
        cnt[1] -= 1
        dfs(idx+1, ans-a[idx])
        # cnt[1] += 1
    if cnt[2] > 0:
        cnt[2] -= 1
        dfs(idx+1, ans*a[idx])
        # cnt[2] += 1
    if cnt[3] > 0:
        cnt[3] -= 1
        dfs(idx+1, int(ans/a[idx]))
        # cnt[3] += 1
        
dfs(1,a[0])
print(max_ans)
print(min_ans)

############################################################################################################################v

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
mx, mn = -1e9, 1e9 # 최대 최소 처음 수

def solve(index, ans, add, sub, mul, div) :
    global mx, mn
    if index >= n :
        mx = max(mx, ans)
        mn = min(mn, ans)
        return
    if add > 0 :
        solve(index+1, ans+a[index], add-1, sub, mul, div)
    if sub > 0 :
        solve(index+1, ans-a[index], add, sub-1, mul, div)
    if mul > 0 :
        solve(index+1, ans*a[index], add, sub, mul-1, div)
    if div > 0 :
        solve(index+1, ans//a[index] if ans > 0 else -((-ans)//a[index]), add, sub, mul, div-1)

solve(1, a[0], op[0], op[1], op[2], op[3])
print(mx)
print(mn)


import sys

input = sys.stdin.readline

def makeAnswer(i):  # i는 연산자리스트의 인덱스
    global min_s, max_s
    if i==n-1:
        number = num[0]
        for j in range(n-1):
            if how[j]==0:
                number += num[j+1]
            elif how[j]==1:
                number -= num[j+1]
            elif how[j]==2:
                number *= num[j+1]
            else:
                number /= num[j+1]
                number = int(number)
        min_s = min(min_s, number)
        max_s = max(max_s, number)
        return

    for j in range(4):  # 0: +, 1: -, 2: *, 3:/
        if way[j]:
            way[j]-=1  # 연산자 한개 빼주고
            how[i]=j 
            makeAnswer(i+1)
            way[j]+=1  # 빼준거 원상복귀


n = int(input())
num = list(map(int, input().split()))
way = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈
how = [0 for _ in range(n-1)]
min_s = 1000000000
max_s = -1000000000
makeAnswer(0)  # 인덱스 0부터 시작
print(max_s)
print(min_s)