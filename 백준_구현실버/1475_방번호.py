import sys
import math

n = sys.stdin.readline()

# 0 ~ 9까지 숫자담은 리스트
num_list = [i for i in range(10)]

# 각 숫자가 몇번 나온지 카운트하고 리스트에 저장
count_list = [0]*10
for num in num_list:
    count_list[num] = n.count(str(num))

# 가장 많이 나온 숫자 저장
max_count = max(count_list)

# 가장 많이 숫자가 6이거나 9이면 
# 6과 9가 나온횟수를 더하고 2로 나눈뒤 올림
if count_list.index(max_count) == 6 or count_list.index(max_count) == 9:
    print(math.ceil((count_list[6] + count_list[9]) / 2))

# 아니면 그냥 가장 큰 count 출력    
else:
    print(max_count)