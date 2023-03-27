# DP - 계단오르기

import sys
n = int(sys.stdin.readline())

stairs = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(stairs[0])
else:
    dp = [0] * n
    #  초기값 설정
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for i in range(2, n):
        # 뒤에서 두번째를 건너 뛴 경우 , 바로 뒤를 건너뛴 경우를 비교해서 할당
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

    print(dp[-1])