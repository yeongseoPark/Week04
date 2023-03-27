# DP (중) - 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline())
lst = list(map(int , sys.stdin.readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))



