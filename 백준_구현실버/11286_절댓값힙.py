import sys

N = int(sys.stdin.readline())

num_list = []
abs_num_list = []

for _ in range(N):
    num = int(sys.stdin.readline())

    if num:
        num_list.append(num)
        abs_num_list.append(abs(num))

    else:
        if num_list:
            min_num = min(abs_num_list)
            abs_num_list.remove(min_num)
            num_list.sort()
            for num in num_list:
                if abs(num) == min_num:
                    num_list.remove(num)
                    print('최솟값', num)
                    break
        else:
            print('비어있음', 0)
