import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [1,2,3]
ans = []

cnt = 0

def perm(ans):          
    global cnt
    if len(ans) > n:
        return
    if sum(ans) == n:    
        cnt += 1        
        if cnt == k:
            for i in range(len(ans)):
                if i == len(ans)-1:
                    print(ans[i])
                else:
                    print('{}+'.format(ans[i]), end='')                
            return
    else:
        for i in range(3):
            ans.append(arr[i])
            perm(ans)
            ans.pop()

perm(ans)
if cnt < k:
    print(-1)