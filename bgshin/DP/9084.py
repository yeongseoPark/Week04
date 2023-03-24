# DP (중) - 동전

import sys

t = int(sys.stdin.readline())

def coin_cnt():
    n = int(sys.stdin.readline())
    coin = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    dp = [[0] * (m+1) for _ in range(n+1)]


    for i in range(n):
        dp[i][0] = 1
        for j in range(1, m+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= coin[i]:
                dp[i][j] += dp[i][j-coin[i]]

    return dp[n-1][m]


for _ in range(t):
    print(coin_cnt())
