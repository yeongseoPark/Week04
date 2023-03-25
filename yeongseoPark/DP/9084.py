import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    coins = list(map(int, input().split()))
    goal  = int(input())

    dp = [1] + [0] * (10000) # 초기상태(동전이 0일때)
    for i in coins:
        for j in range(i, 10001):
            dp[j] += dp[j-i]
    
    print(dp[goal])



        


    