# DP - 병사 배치하기 

import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

# def exeption():
#     dp = [0] * (n)
#     cnt = 0
#     for i in range(n):
        
#         if i == 0:
#             if lst[i] < lst[i+1]:
#                 dp[i] = lst[i+1]
#                 cnt += 1
#             else:    
#                 dp[i] = lst[i]
#         if i == n-1:
#             if lst[i] < lst[i-1]:
#                 dp[i] = lst[i]        
#             else:
#                 cnt += 1
#         if lst[i] < lst[i-1]:
#             if lst[i] < lst[i+1]:
#                 dp[i] = lst[i+1]
#                 cnt += 1
#             else:    
#                 dp[i] = lst[i]
#     return cnt

# print(exeption())

def count_soldiers():
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if lst[j] > lst[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return n - max(dp)

print(count_soldiers())