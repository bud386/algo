import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

friends = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

que = deque([1])

invited = []

# 자기 자신한번, 자기 친구수 만큼 한번씩
# 1. 자신의 친구 탐색해서 리스트에 추가
# 2. 자신의 친구의 친구 리스트에 추가 (len[friends[1]])
for _ in range(1 + len(friends[1])):
    next = que.popleft()
    for i in friends[next]:
        que.append(i)
        invited.append(i)

print(len(set(invited)) - 1)    # set써서 중복된 1이랑 친구들 빼고, 자기 자신도 빼줌.



# visited = [0 for _ in range(n+1)]
# print(invited)

# print (n, m, friends, visited)