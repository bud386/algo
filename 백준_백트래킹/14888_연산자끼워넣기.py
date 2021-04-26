import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
pl, mi, mul, di  = map(int, input().split())
max_ans = -9999999999
min_ans = 9999999999

def cal(ans, idx, pl, mi, mul, di):
    global max_ans, min_ans
    if idx == N:
        max_ans = max(ans, max_ans)
        min_ans = min(ans, min_ans)
        return

    else:
        if pl:
            cal(ans+num[idx], idx+1, pl-1, mi, mul, di)
        if mi:
            cal(ans-num[idx], idx+1, pl, mi-1, mul, di)
        if mul:
            cal(ans*num[idx], idx+1, pl, mi, mul-1, di)
        if di:
            if ans < 0:
                ans = -(abs(ans)//num[idx])
            else:
                ans //= num[idx]
            cal(ans, idx+1, pl, mi, mul, di-1)

cal(num[0], 1, pl, mi, mul, di)
print(max_ans)
print(min_ans)

