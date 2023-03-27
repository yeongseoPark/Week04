import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * (4) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 4):
        if j == 1:
            dp[i][j] = min(dp[i-1][j+1], dp[i-1][j+2]) + cost[i-1][j-1]
        
        elif j == 2:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j+1]) + cost[i-1][j-1]

        else: 
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j-2]) + cost[i-1][j-1]

print(min(dp[n][1:]))