import sys
input = sys.stdin.readline

N = int(input())
L = {}
R = {}
for i in range(N):
    p, l, r = map(str, input().split())
    L[p] = l
    R[p] = r

# print(tree)

ans = ['','','']
def preorder(node):
    global ans
    if node != '.':
        ans[0] += node
        preorder(L[node])
        preorder(R[node])

def inorder(node):
    global ans
    if node != '.':
        inorder(L[node])
        ans[1] += node
        inorder(R[node])

def postorder(node):
    global ans
    if node != '.':
        postorder(L[node])
        postorder(R[node])
        ans[2] += node

preorder('A')
inorder('A')
postorder('A')

for i in ans:
    print(i)