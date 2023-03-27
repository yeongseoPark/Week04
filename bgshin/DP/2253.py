# DP (상) - 점프

# 1. 문제 이해: 문제 설명을 분석하고 제약 조건, 입력 및 원하는 출력을 이해합니다.
# 2. DP 상태 정의: DP 상태를 dp[위치][점프]로 정의합니다. 이는 현재 점프 파워로 위치에 도달하는 데 필요한 최소 점프 수를 나타냅니다.
# 3. DP 테이블 초기화: DP 테이블을 시작 위치를 제외한 모든 위치 및 점프력에 대해 큰 값(예: 1e9)으로 초기화합니다. dp[1][1] = 0으로 설정하세요. 개구리는 점프력이 1인 첫 번째 위치에서 시작합니다.
# 4. DP 테이블을 통한 반복: 각 위치 및 점프 파워를 반복하고 다음 규칙을 사용하여 테이블을 업데이트합니다.
#     4-1. 현재 위치의 돌이 너무 작으면 건너뛰고 다음 위치로 진행합니다.
#     4-2. 개구리가 현재 점프 파워(즉, currentPosition + jumpPower)로 도달할 수 있는 다음 위치를 계산합니다.
#     4-3. dp[nextPosition][jumpPower]와 dp[currentPosition][jumpPower] + 1 사이의 최소값으로 DP  테이블을  업데이트합니다.
#     4-4. dp[nextPosition][jumpPower + 1]과 dp[currentPosition][jumpPower] + 1 사이의 최소값으로 DP 테이블을 업데이트합니다.
# 5. 최소 점프 수 찾기: DP 테이블의 마지막 행(즉, 마지막 위치)을 반복하고 최소값을 찾습니다. 이 값은 강의 반대편에 도달하는 데 필요한 최소 점프 수를 나타 냅니다.
# 6. 결과 출력: 최소 점프 횟수를 출력하거나 개구리가 반대편에 도달하는 것이 불가능하면 -1을 출력합니다.

import sys

n , k= map(int, sys.stdin.readline().split())

lst = [int(sys.stdin.readline()) for _ in range(k)]

    
dp = [0] * (n+1)



-------------

from sys import stdin

N, stone_n = map(int, stdin.readline().split())

stone = set()
for _ in range(stone_n):
    stone.add(int(stdin.readline().rstrip()))

dp  = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]

dp[1][0] = 0
for i in range(2, N+1):
    if i in stone:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) +1


ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)