import sys 
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

# before_top = nums[0]
# length = [1] # 처음 숫자에서는 LIS길이 1

# for i in range(1, len(nums)):
#     if nums[i] > before_top:
#         before_top = nums[i]
#         length.append(length[-1] + 1)
#     else:
#         length.append(length[-1])

# print(length[-1])

# # 반례
# # 1 3 5 100 101 77 78 101
# # 1 3 5 77 78 101이 젤 긴데 
# # 1 3 5 100 101로 답 나옴 

dp = [1] * (n)
for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))