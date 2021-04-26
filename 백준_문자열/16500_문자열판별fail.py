# dp

import sys
input = sys.stdin.readline

s = input().strip()
# s = 'softwaresoftwarecontest softwares'
# print(s)

n = int(input())
word = []
for _ in range(n):
    word.append(input().strip())

word.sort(key=len)
# print(word)
for i in range(n-1, -1, -1):
    print(s, word[i])
    s = s.replace(word[i], ' ')

print(s)
if s.strip():
    print(0)
else:
    print(1)