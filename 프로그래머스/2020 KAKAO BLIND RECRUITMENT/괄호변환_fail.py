def solution(p):
    w = []
    v = []
    open_cnt = 0
    close_cnt = 0
    for i in p:
        if i == '(':
            open_cnt += 1
        else:
            close_cnt += 1
        w.append(i)
        if open_cnt == close_cnt:
            break
        
    answer = ''
    return answer