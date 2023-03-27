n = int(input())

dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

if n == 1 or n == 2:
    print(dp[n])
    exit()

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])