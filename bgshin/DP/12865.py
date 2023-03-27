# DP (중) - 평범한 배낭

import sys

n ,k = map(int , sys.stdin.readline().split())

lst = [list(map(int , sys.stdin.readline().split())) for _ in range(n)]

def packaing():
    
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(k+1):
            # 배낭에 담을 수 있는 경우
            if lst[i-1][0] <= j:
                # 이전 단계의 가치와 현재 물건의 가치와 남은 무게에서의 가치 합계 중 큰 값
                dp[i][j] = max((dp[i-1][j]),(dp[i-1][j-lst[i-1][0]] + lst[i-1][1])) 
            else:
                # 이전 단계의 가치로 설정
                dp[i][j] = dp[i-1][j]


    return dp[n][k]
       

print(packaing())