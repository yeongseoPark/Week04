import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if sol[j] > sol[i]: # = 있으면 안되더라고..
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))