import sys
input = sys.stdin.readline

k = int(input())    # 부등호 문자의 개수
formula = list(input().split()) # 부등호
visited = [0] * 10

# 부등호 성립하는지 확인
def check(pick):
    for i in range(len(pick)-1):        
        if formula[i] == '<':
            if pick[i] < pick[i+1]:
                continue
            else:
                return False
        else:
            if pick[i] > pick[i+1]:
                continue
            else:
                return False
    return True

big = 0
small = 99999999999
small_list = '' # 가장 작은수의 경우 int형으로 저장할때 앞에 0이 누락되는 경우가 생겨서

pick = []
def permutation():
    global big, small, small_list
    if len(pick) >= 2:
        if check(pick) == False:
            return

    if len(pick) == k + 1:
        if check(pick):
            big = max(big, int(''.join(map(str, pick))))
            if small > int(''.join(map(str, pick))):
                small = int(''.join(map(str, pick)))
                small_list = ''.join(map(str, pick))
        return
    
    for i in range(10):
        if visited[i] == 0:
            visited[i] = 1
            pick.append(i)
            permutation()
            visited[i] = 0
            pick.pop()


permutation()            
print(big, small_list, sep="\n")
