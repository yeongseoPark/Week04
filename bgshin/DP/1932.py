# DP - 정수 삼각형

import sys

n = int(sys.stdin.readline())

trn = []
for _ in range(n):
    trn.append(list(map(int, sys.stdin.readline().split())))

for idx, i in enumerate(trn):
    while True:
        if len(trn[idx]) <= n:
            trn[idx].append(0)
        else:
            break

def int_trn () :
    
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[1][1] = trn[0][0]

    for i in range(2,n+1):
        for j in range(1,n+1):
            if j == 1:
                dp[i][j] = dp[i-1][j] + trn[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j-1] + trn[i-1][j-1], dp[i-1][j] + trn[i-1][j-1]) 

    return(max(dp[n]))

print(int_trn())