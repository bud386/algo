import sys
from collections import defaultdict
input = sys.stdin.readline

cnt_dict = defaultdict(int)
cnt = 0
while True:
    tree = input().strip()
    if tree == "": 
        break
    cnt_dict[tree] += 1
    cnt += 1            


trees = sorted(cnt_dict)
for tree in trees:
    # print(tree, round(cnt_dict[tree]/cnt*100, 4)) 30.0000,    
    print('{} {:.4f}'.format(tree, cnt_dict[tree]/cnt*100))
