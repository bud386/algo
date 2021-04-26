import sys
# from collections import deque
# import copy

t = int(sys.stdin.readline())

for _ in range(t):

    n, m = map(int, sys.stdin.readline().split())
    que = list(map(int, sys.stdin.readline().split()))
    
    # 문제에서 출력할 m번째 문서를 체크하기 위한 리스트
    doc_order_que = [i for i in range(n)]

    count = 0

    while que:
        
        # 첫번째 차례에 있는 문서의 중요도가 가장 높은게 아니면
        if que[0] < max(que):
            
            # que의 맨뒤로 보내고
            que += [que.pop(0)]
            
            # 문서의 순서를 담은 que에서도도 맨 뒤로 보낸다.
            doc_order_que += [doc_order_que.pop(0)]

        # 중요도가 가장 높은 문서일때
        elif que[0] == max(que):
            count += 1

            # 만약 처음에 m 번째의 문서가 프린트될 조건이면:
            if doc_order_que[0] == m:
                break
            
            # 프린트하고 pop으로 없앰
            else:
                que.pop(0)
                doc_order_que.pop(0)

    print(count)

