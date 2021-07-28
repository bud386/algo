import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())


a_num = list(map(int, sys.stdin.readline().split()))

num = 0
square = 0
for i in range(m-1, -1, -1):
    num += a**square * a_num[i]
    square += 1

b_num = []
while num:
    b_num.append(num % b)
    num //= b

print(*reversed(b_num))
