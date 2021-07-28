import sys
import copy
from collections import deque


T = int(sys.stdin.readline())

# def R(num_list, cnt):
#     if cnt % 2:
#         return num_list.reverse()
#     else:
#         return num_list

def D(num_list, cnt):
    if cnt % 2:
        num_list.pop()
    else:
        num_list.popleft()
    
    return num_list



for _ in range(T):
    p = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    num_list = sys.stdin.readline()
    num_list = deque(num_list[1:-2].split(','))

    result = copy.deepcopy(num_list)
    
    cnt_R = 0
    for func in p:
        if func == 'R':
            cnt_R += 1
        elif func == 'D':
            if n != 0:
                if num_list:
                    result = D(num_list, cnt_R)
                else:
                    result = 'error'
                    break
            else:
                result = 'error'
                break       
    

    if result == 'error':
        print(result)
    else:
        if cnt_R % 2:
            result.reverse()
        print('['+ ','.join(result) +']')


    
    

    

