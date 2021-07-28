import sys

k = int(sys.stdin.readline())

money_list = []

for i in range(k):
    money = int(sys.stdin.readline())
    if money:
        money_list.append(money)
    else:
        # 0이 먼저 들어오면 오류
        if len(money_list) > 0:
            money_list.pop()

print(sum(money_list))

