import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    dp = [i for i in sticker]
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for c in range(2, n):
        dp[0][c] = max(dp[1][c-1]+dp[0][c], dp[1][c-2]+dp[0][c])
        dp[1][c] = max(dp[0][c-1]+dp[1][c], dp[0][c-2]+dp[1][c])
    
    
    ans = max(max(dp[0]), max(dp[1]))        
    print(ans)

    
            
                

