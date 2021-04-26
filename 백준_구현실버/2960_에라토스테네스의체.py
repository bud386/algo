import sys
import copy

n, k = map(int, sys.stdin.readline().split())

num_list = [i for i in range(2,n+1)]

count = 0
flag = 0

while num_list:
    # 아직 지우지 않은 가장 작은 수
    p = num_list[0]
    # p의 배수를 담을 리스트
    remove_list = []
    for num in num_list:
        if num % p == 0:
            remove_list.append(num)
            count += 1
            if count == k:
                print(num)
                flag = 1
                break
    if flag == 1:
        break
    num_list = [i for i in num_list if i not in remove_list]

  



