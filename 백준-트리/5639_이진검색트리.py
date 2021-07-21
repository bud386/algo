import sys
input = sys.stdin.readline

# P = {}
L = {}
R = {}
before = 0
while True:
    
    try:
        i=int(input())
        if i > before:
            L[before] = i
        else:
            R[before] = i
        before = i
    except:
        break
    
print(L, R)



# def preorder(node):
#     global ans
#     if node != '':
#         print(node)
#         preorder(L[node])
#         preorder(R[node])