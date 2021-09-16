import sys
inpur = sys.stdin.readline

K = int(input())
orders = list(map(int, input().split()))
tree =  [[] for _ in range(K)]

def make_tree(buildings, depth):
    if depth == K:
        return
    root = len(buildings) // 2
    tree[depth].append(buildings[root])
    make_tree(buildings[:root], depth + 1)
    make_tree(buildings[root+1:], depth + 1)

make_tree(orders, 0)
for nodes in tree:
    print(*nodes)




