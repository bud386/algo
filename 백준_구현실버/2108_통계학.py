import sys
import math

n = int(sys.stdin.readline())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

# 최빈값
if n == 1:
    max_num = num_list[0]
# 최빈값
else:
    # 각 숫자를 카운트해서 list해 튜플 형태로 담아줌 (숫자, 카운트)
    set_num_list = list(set(num_list))
    count_num_list = []

    for i in set_num_list:
        count_num_list.append((i, num_list.count(i)))

    # (2번쨰 인덱스인 카운트를 기준으로 정렬)
    count_num_list.sort(key=lambda x:-x[1])
    

    max_num_list = []
    # 만약 정렬된 리스트의 첫 카운트 값이 그 다음거랑 같지않으면
    # 유일한 가장 큰 카운트 값이기 때문에 그 카운트 값에 해당하는 숫자를 최빈값으로 설정
    if count_num_list[0][1] != count_num_list [1][1]:
        max_num = count_num_list[0][0]
    
    # 만약 최빈값이 많다면 
    # 같은 count를 가진 숫자와 count를 모아서 다시 정렬하고 (이 때는 카운트가 아닌 숫자로 정렬)
    # 그리고 정렬된 리스트에서 2번째 순서의 숫자값을 최빈값으로 저장
    else:
        for count_num in count_num_list:
            if count_num[1] == count_num_list[0][1]:
                max_num_list.append(count_num)
            else:
                break
        max_num_list.sort(key=lambda x:x[0])
        max_num = max_num_list[1][0]


print(round(sum(num_list)/n))
print(sorted(num_list)[n//2])
print(max_num)
print(max(num_list)-min(num_list))
