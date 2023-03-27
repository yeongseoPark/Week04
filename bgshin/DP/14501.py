# DP - 퇴사

import sys

n = int(sys.stdin.readline())

schedule = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# for i in range(n):
#     time ,cost  = map(int, sys.stdin.readline().split())
#     if n-(time+i) < 0:
#         pass
#     else:
#         schedule.append([time,cost])

def counseling():
    dp = [0] * (n+1)

    for i in range(n):
        for j in range(i + schedule[i][0],n+1):
            if dp[j] < dp[i] + schedule[i][1]:
                dp[j] = dp[i] + schedule[i][1]

    return(dp[-1])


print(counseling())