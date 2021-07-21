
def makeIt(how, row, col, cnt):
    global result
    if cnt+2*n-2-row-col >= result:
        return

    if row == n-1 and col == n-1:
        if board[row][col] <= 2 and how == 3 or board[row][col] > 2 and how == 0:
            result = min(result, cnt)
        return
    
    if how == 0 or how == 2:
        if board[row][col] > 2:
            if col > 0 and not visit[row][col-1] and board[row][col-1]:
                visit[row][col-1] = 1
                makeIt(1, row, col-1, cnt+1)
                visit[row][col-1] = 0
            if col < n-1 and not visit[row][col+1] and board[row][col+1]:
                visit[row][col+1] = 1
                makeIt(3, row, col+1, cnt+1)
                visit[row][col+1] = 0
        elif how == 0:
            if row < n-1 and not visit[row+1][col] and board[row+1][col]:
                visit[row+1][col] = 1
                makeIt(0, row+1, col, cnt+1)
                visit[row+1][col] = 0
        elif how == 2:
            if row > 0 and not visit[row-1][col] and board[row-1][col]:
                visit[row-1][col] = 1
                makeIt(2, row-1, col, cnt+1)
                visit[row-1][col] = 0
    else:
        if board[row][col] > 2:
            if row > 0 and not visit[row-1][col] and board[row-1][col]:
                visit[row-1][col] = 1
                makeIt(2, row-1, col, cnt+1)
                visit[row-1][col] = 0
            if row < n-1 and not visit[row+1][col] and board[row+1][col]:
                visit[row+1][col] = 1
                makeIt(0, row+1, col, cnt+1)
                visit[row+1][col] = 0
        elif how == 1:
            if col > 0 and not visit[row][col-1] and board[row][col-1]:
                visit[row][col-1] = 1
                makeIt(1, row, col-1, cnt+1)
                visit[row][col-1] = 0
        elif how == 3:
            if col < n-1 and not visit[row][col+1] and board[row][col+1]:
                visit[row][col+1] = 1
                makeIt(3, row, col+1, cnt+1)
                visit[row][col+1] = 0


t = int(input())

ans = []

for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    result = 2500
    makeIt(3, 0, 0, 1)
    ans.append(f"#{tc} {result}")
print("\n".join(ans))


###############################################################

t = int(input())

def makeIt(row, col, bit, cnt):

    if col == w-1: return 0
    if row >= h-1:
        b = 0
        for r in range(h):
            if board[r][col+1]:
                b |= (1<<r)
        return cnt + makeIt(0, col+1, b, 0)
    
    if row == 0 and dp[col][bit] >= 0: return dp[col][bit]

    result = 0
    for r in range(row, h-1):
        if board[r][col]==0 and board[r+1][col]==0 and board[r][col+1]==0 and board[r+1][col+1]==0:
            board[r][col]=board[r+1][col]=board[r][col+1]=board[r+1][col+1] = 1
            result = max(result, makeIt(r+2, col, bit, cnt+1))
            board[r][col]=board[r+1][col]=board[r][col+1]=board[r+1][col+1] = 0
            
    result = max(result, makeIt(h, col, bit, cnt))
    if row == 0: dp[col][bit] = result
    return result



ans = []  
for tc in range(1, t+1):
    h, w = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    
    dp = [[-1 for _ in range(1<<h)] for _ in range(w)]
    b = 0
    for r in range(h):
        if board[r][0]:
            b |= (1<<r)
    
    ans.append(f"#{tc} {makeIt(0,0,b,0)}")

print("\n".join(ans))

####################################################################################################

def makeIt(i, way, bit):

    if dp[i][way][bit]>=0: return dp[i][way][bit]
    result = 0
    for j, w in link[i][way]:
        if bit & (1<<j) == 0:
            result = max(result, makeIt(j, w, bit|(1<<j)))

    dp[i][way][bit] = boxes[i][way] + result
    return dp[i][way][bit]

t = int(input())
ans = []
for tc in range(1, t+1):
    n = int(input())

    boxes = [list(map(int,input().split(" "))) for _ in range(n)]

    box_3 = [[(min(box[1], box[2]), max(box[1], box[2])), 
    (min(box[0], box[2]), max(box[0], box[2])), 
    (min(box[0], box[1]), max(box[0], box[1]))] for box in boxes]

    link = [[[] for _ in range(3)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            for a in range(3):
                for b in range(3):
                    if box_3[i][a][0]>=box_3[j][b][0] and box_3[i][a][1]>=box_3[j][b][1]:
                        link[i][a].append((j, b))
                    if box_3[j][a][0]>=box_3[i][b][0] and box_3[j][a][1]>=box_3[i][b][1]:
                        link[j][a].append((i, b))

    dp = [[[-1]*(1<<n) for _ in range(3)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(3):
            result = max(result, makeIt(i, j, 1<<i))
    ans.append(f"#{tc} {result}")
print("\n".join(ans))

