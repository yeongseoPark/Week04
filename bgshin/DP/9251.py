# DP (중) - LCS

import sys

n = str(sys.stdin.readline().strip())
m = str(sys.stdin.readline().strip())

def lcs(n,m):
    # DP 테이블을 초기화
    dp = [[0] * (len(m)+1) for _ in range((len(n)+1))]

    for i in range(1, len(n)+1):
       for j in range(1, len(m)+1):
            # 두 문자열의 각 문자를 비교
            if n[i-1] == m[j-1]:
                # 같다면 현재 위치의 값을 갱신
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # 다르다면 큰 값을 현재 위치의 값으로 설정
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # dp의 마지막 원소 값을 출력
    return dp[len(n)][len(m)]

print(lcs(n,m))
