import sys
input = sys.stdin.readline

N = int(input()) +1

def permutation(length):
    global N    
    if len(pick) == length:        
        N -= 1
        if N == 0:
            print(''.join(map(str, pick)))
            exit()     
        return

    for i in range(10):
        if visited[i] == 0:
            if pick == [] or pick[-1] > i:
                visited[i] = 1
                pick.append(i)                
                permutation(length)
                visited[i] = 0
                pick.pop()

pick = []
visited = [0] *10
for i in range(1, 11):
    permutation(i)
if N:
    print(-1)



###
dList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = 10
for d in dList:
    t = d % a
    if d != 0 and d != 1:
        for i in range(t):
            dList.append((d*10+i))

n = int(input())
if n < len(dList):
    print(dList[n])
else:
    print(-1)