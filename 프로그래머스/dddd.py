
def solution(orders, course):
    answer = {}
    for order in orders:
        for menu_cnt in course:
            n = len(order)
            pick = []     
            ret = comb(0, 0, order, menu_cnt, n, pick, answer)
    
    for key, val in 
            
    print( answer)

def comb(k, start, arr, menu_cnt, n, pick, answer):
    if k == menu_cnt:
        pick = "".join(pick)
        if pick in answer:
            answer[pick] += 1
        else:
            answer[pick] = 1
        return

    for i in range(start, n):
        pick.append(arr[i])
        comb(k + 1, i + 1, arr, menu_cnt, n, pick, answer)
        pick.pop()


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])



alpha = [0 for _ in range(26)]
result = []
max_cnt = 0
max_arr = []
check = [False for _ in range(26)]

def solution(orders, course):
    global check
    global result
    global max_cnt
    global max_arr
    global alpha

    answer = []

    for s in orders:
        for i in range(len(s)):
            alpha[ord(s[i]) - 65] += 1

    for c in course:
        comb(0, 0, c, orders)
        for a in max_arr:
            answer.append(a)
        result = []
        max_cnt = 0
        max_arr = []
        check = [False for _ in range(26)]
       
    answer.sort()
    return answer

def comb(idx, cnt, total, orders):
    global check
    global result
    global max_cnt
    global max_arr
    global alpha

    if cnt == total:
        tmp = isCnt(orders, result)
        join_str = "".join(result)
        # print("tmp: ", tmp, "joion_str = ", join_str)
        if tmp >= 2 and max_cnt < tmp:
            max_arr.clear()
            max_cnt = tmp
            max_arr.append(join_str)
        elif tmp >= 2 and max_cnt == tmp:
            max_arr.append(join_str)
        # print("max_cnt = ", max_cnt, "max_arr = ", max_arr)
        return

    for i in range(idx, 26):
        if alpha[i] != 0 and not check[i]:
            result.append(chr(i+65))
            check[i] = True
            comb(i+1, cnt+1, total, orders)
            check[i] = False
            result = result[:-1]  


def isCnt(orders, result):
    count = 0
    
    for s in orders:
        no = False
        for c in result:
            if c not in s: 
                no = True
                break
        if not no:
            count += 1

    return count