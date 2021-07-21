import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find_solution(l_in, r_in, l_post, r_post):

    if l_in > r_in or l_post > r_post:
        return

    root = post_order[r_post]
    print(root, end = " ")

    S_idx = idx[root]
    left = S_idx - l_in

    find_solution(l_in, S_idx - 1, l_post, (l_post + left) - 1)
    find_solution(S_idx + 1, r_in, l_post + left, r_post - 1)


N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

idx = [0] * (N+1)
for i in range(N):
    idx[in_order[i]] = i

find_solution(0, N - 1, 0, N - 1)