import sys
input = sys.stdin.readline
end_day = int(input())
sangdam_list = []
for _ in range(end_day):
    sangdam_list.append(list(map(int, input().split())))
print(sangdam_list)
dp = [0]* (end_day+1)

print(dp)

for i in range(0, end_day):
    print(i+ sangdam_list[i][0])
    for j in range(i+sangdam_list[i][0], end_day+1):
        print(i+sangdam_list[i][0], end_day+1)
        if dp[j] < dp[i] + sangdam_list[i][1]:
            dp[j] = dp[i] + sangdam_list[i][1]
    print('yala')
    print(dp)
print(dp[-1])