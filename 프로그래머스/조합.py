arr = "ABCDE"
pick = [" "] * len(arr)


def comb(n, r):
    print(n, r)
    if n < r:
        return
    if r == 0:
        print(pick)
        return

    pick[r - 1] = arr[n - 1]
    # print(pick, 'asdasd', n, r)
    comb(n - 1, r - 1)
    comb(n - 1, r)


comb(5, 3)


arr = "ABCDE"
pick = []
n = len(arr)
r = 3


def comb(k, start):
    if k == r:
        print(pick)
        return

    for i in range(start, n):
        pick.append(arr[i])
        comb(k + 1, i + 1)
        pick.pop()


comb(0, 0)
