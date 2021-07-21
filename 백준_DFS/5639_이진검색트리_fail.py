import sys
input = sys.stdin.readline

def post_order(start, end):
    
    if start > end:
        return

    # 루트 노드
    root = pre_order[start]
    idx = start + 1

    # root보다 커지는 지점을 찾는 과정  
    while idx <= end:
        if pre_order[idx] > root:
            break
        idx += 1


    post_order(start + 1, idx - 1)    
    post_order(idx, end)
    print(root)


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

post_order(0, len(pre_order) - 1)