import sys

N = sys.stdin.readline().strip()

cnt = 0
# 몇자리 숫자인지
for i in range(len(N)):
    # 마지막 자리수(3자리 숫자이면 3 * N -100)
    if i == len(N)-1:
        cnt += (i+1) * (int(N) - 10**i + 1)
    # 9 90 900
    else:
        cnt += (i+1)*9*(10**i)
        
print(cnt)