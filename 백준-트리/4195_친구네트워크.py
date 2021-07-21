import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(x, y):    
    x = find(x)
    y = find(y)   
    if x != y: 
        parents[x] = y
        friends_cnt[y] += friends_cnt[x]
    

for tc in range(int(input())):
    F = int(input())
    parents = {}
    friends_cnt = {}
    # relation = []
    for _ in range(F):
        a, b = input().split()
        
        if a not in parents:
            parents[a] = a
            friends_cnt[a] = 1 
        if b not in parents:
            parents[b] = b
            friends_cnt[b] = 1 
        
        union(a, b)
        # 뒤에 입력된 친구를 부모로 잡았기 때문에
        print(friends_cnt[find(b)])
        # relation.append([a, b])
        

    # print(friends)
    # print(parents)