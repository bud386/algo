N = 5
choice = [0] * 3
def backtrack(idx, row_sum):
    if row_sum > N: 
        print(idx, row_sum, '끝')
        return
    if idx == 3:
        if row_sum == N:
            print(row_sum, '-->', choice)
    else:
        for i in range(1, N - 2 + 1):
            choice[idx] = i
            print(idx +1, row_sum + i, '시작')
            backtrack(idx + 1, row_sum + i)

backtrack(0, 0)