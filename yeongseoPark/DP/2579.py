import sys
input = sys.stdin.readline
n = int(input())
stairs = [int(input()) for _ in range(n)]

if n <= 2:
    print(sum(stairs))
    exit()
elif n == 3:
    print(stairs[2] + max(stairs[0], stairs[1]))
    exit()

dp = [0] * 300
dp[0] = stairs[0]
dp[1] = stairs[0] + stairs[1]
dp[2] = stairs[2] + max(stairs[0], stairs[1])

for i in range(3, n):
    dp[i] = stairs[i] + max(dp[i-3] + stairs[i-1], dp[i-2])

print(dp[n-1])