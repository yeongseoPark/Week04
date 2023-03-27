import sys

input = sys.stdin.readline

n = int(input())

day = [] # 걸리는 시간 
cost = [] # 이득
dp = []

for _ in range(n):
    due, profit = map(int, input().split())
    day.append(due)
    cost.append(profit)
    dp.append(profit)
dp.append(0)

for i in range(n-1, -1, -1):
    if day[i] + i > n: # 데드라인이 기한을 넘어감
        dp[i] = dp[i+1] # 일을 할수없음
    else:
        dp[i] = max(dp[i+1], cost[i] + dp[i+day[i]])

print(dp[0])