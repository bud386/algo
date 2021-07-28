import sys

n = int(sys.stdin.readline())

wh_list = []
for i in range(n):
    wh_list.append(list(map(int, sys.stdin.readline().split())))

# 각자의 rank를 저장할 리스트
rank = [1]*n

# (n명의 사람) 
for i in range(n):
    # (자기 자신(i번째와 i번째)과 이미 비교했던 사람 빼고, 다음사람(j번째)이랑만 비교하기 위해서)
    for j in range(i+1, n):
        # i번째가 더 작으면 i번째의 rank +1 
        if wh_list[i][0] < wh_list[j][0] and wh_list[i][1] < wh_list[j][1]:
            rank[i] += 1
        # i번째가 더 크면 j번째 사람(비교대상)의 rank +1
        elif wh_list[i][0] > wh_list[j][0] and wh_list[i][1] > wh_list[j][1]:
            rank[j] += 1

print(*rank) 


# rank[wh_list.index(wh_list[i])] += 1 ==> 이걸 이용하면 몸무게와 키가 같은 사람이 있을때 오류 생김!!!



# import sys
# n = int(sys.stdin.readline())

# wh_list = []
# for i in range(n):
#     wh_list.append(list(map(int, sys.stdin.readline().split())))
    

# ans = [1]*n
# rank_list = []

# for wh_1 in wh_list:
#     rank = 1

#     for wh_2 in wh_list:
#         if wh_1[0] < wh_2[0] and wh_1[1] < wh_2[1]:
#             # ans[wh_list.index(wh_1)] += 1 ==> 이걸 이용하면 몸무게와 키가 같은 사람이 있을때 문제가 생김!!!
#             ans[wh_list.index(wh_1)] += 1
#             rank += 1
    
#     rank_list.append(rank)

# print(rank_list)
# print(ans)
