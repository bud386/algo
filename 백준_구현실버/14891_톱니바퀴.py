# 시계 (1) : gear[1] = [gear[1].pop()] + gear[1]
# 반시계 (-1) gear[1] += [gear[1].pop(0)]

# gear[2] = [gear[2].pop()] + gear[2]
# gear[2] += [gear[2].pop(0)]

# gear[3] = [gear[3].pop()] + gear[3]
# gear[3] += [gear[3].pop(0)]

# gear[4] = [gear[4].pop()] +gear[4]
# gear[4] += [gear[4].pop(0)]

import sys

gear = {}
for i in range(1,5):
    gear[i] = list(map(int, sys.stdin.readline().strip()))

k = int(sys.stdin.readline())

# 몇번째 톱니바퀴에서 무슨 방향으로 돌릴지 저장
turn_list = []
for _ in range(k):
    turn_list.append(list(map(int, sys.stdin.readline().split())))

for i in turn_list:

    if i[0] == 1 and i[1] == 1:
        if gear[1][2] != gear[2][6]:
            if gear[2][2] != gear[3][6]:
                if gear[3][2] != gear[4][6]:
                    gear[4] += [gear[4].pop(0)]
                gear[3] = [gear[3].pop()] + gear[3]
            gear[2] += [gear[2].pop(0)]
        gear[1] = [gear[1].pop()] + gear[1]
    
    elif i[0] == 1 and i[1] == -1:
        if gear[1][2] != gear[2][6]:
            if gear[2][2] != gear[3][6]:
                if gear[3][2] != gear[4][6]:
                    gear[4] = [gear[4].pop()] +gear[4]
                gear[3] += [gear[3].pop(0)]
            gear[2] = [gear[2].pop()] + gear[2]
        gear[1] += [gear[1].pop(0)]
    
    elif i[0] == 2 and i[1] == 1:
        if gear[2][2] != gear[3][6]:
            if gear[3][2] != gear[4][6]:
                gear[4] = [gear[4].pop()] +gear[4]
            gear[3] += [gear[3].pop(0)]
        if gear[2][6] != gear[1][2]:
            gear[1] += [gear[1].pop(0)]
        gear[2] = [gear[2].pop()] + gear[2]
        
    elif i[0] == 2 and i[1] == -1:
        if gear[2][2] != gear[3][6]:
            if gear[3][2] != gear[4][6]:
                gear[4] += [gear[4].pop(0)]
            gear[3] = [gear[3].pop()] + gear[3]
        if gear[2][6] != gear[1][2]:
            gear[1] = [gear[1].pop()] + gear[1]
        gear[2] += [gear[2].pop(0)]
    
    elif i[0] == 3 and i[1] == 1:
        if gear[3][6] != gear[2][2]:
            if gear[2][6] != gear[1][2]:
                gear[1] = [gear[1].pop()] + gear[1]
            gear[2] += [gear[2].pop(0)]
        if gear[3][2] != gear[4][6]:
           gear[4] += [gear[4].pop(0)]
        gear[3] = [gear[3].pop()] + gear[3]
    
    elif i[0] == 3 and i[1] == -1:
        if gear[3][6] != gear[2][2]:
            if gear[2][6] != gear[1][2]:
                gear[1] += [gear[1].pop(0)]
            gear[2] = [gear[2].pop()] + gear[2]
        if gear[3][2] != gear[4][6]:
           gear[4] = [gear[4].pop()] +gear[4]
        gear[3] += [gear[3].pop(0)]
    
    elif i[0] == 4 and i[1] == 1:
        if gear[4][6] != gear[3][2]:
            if gear[3][6] != gear[2][2]:
                if gear[2][6] != gear[1][2]:
                    gear[1] += [gear[1].pop(0)]
                gear[2] = [gear[2].pop()] + gear[2]
            gear[3] += [gear[3].pop(0)]
        gear[4] = [gear[4].pop()] +gear[4]
        
    elif i[0] == 4 and i[1] == -1:
        if gear[4][6] != gear[3][2]:
            if gear[3][6] != gear[2][2]:
                if gear[2][6] != gear[1][2]:
                    gear[1] = [gear[1].pop()] + gear[1]
                gear[2] += [gear[2].pop(0)]
            gear[3] = [gear[3].pop()] + gear[3]
        gear[4] += [gear[4].pop(0)]

sum = gear[1][0] + gear[2][0]*2 + gear[3][0]*4 + gear[4][0]*8       

print(sum)