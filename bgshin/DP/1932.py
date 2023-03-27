# DP - 정수 삼각형

import sys

n = int(sys.stdin.readline())

trn = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

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


# import sys
# input = sys.stdin.readline

# n = int(input())
# start = int(input())
# if n == 1:
#     print(start)
# else:
#     second = list(map(int, input().split()))
#     second[0] += start
#     second[1] += start

#     before = [second[0], second[1]]
#     for i in range(1, n-1):
#         temp = []
#         cur = list(map(int, input().split()))
#         temp.append(before[0] + cur[0])
#         for j in range(1, i+1):
#             temp.append(max(cur[j]+before[j-1], cur[j]+before[j]))
        
#         temp.append(before[len(before)-1] + cur[len(cur)-1])
#         before = temp[:]

#     print(max(before))