import sys
input = sys.stdin.readline
end_day = int(input())
sangdam_list = []
for _ in range(end_day):
    sangdam_list.append(list(map(int, input().split())))
print(sangdam_list)
dp = [[0]* end_day for _ in range(end_day)]

for i in range(end_day):
#end day 전까진 스탬프 박기
    # dp[i][0], dp[i][1], dp[i][2] 에 스탬프 박기
    for idx, j in enumerate(range(i, i + sangdam_list[i][0])):
        print(idx, j)
        try:
            if idx == 0:
                dp[i][j] = dp[i][j-1] + sangdam_list[i][1]
            elif idx >= 1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        except:
            if idx == 0:
                dp[i][j] = sangdam_list[i][1]
            elif idx >= 1:
                try:
                    dp[i][j] = sangdam_list[i][j-1]
                except:
                    continue
# 
#  
#
#
for i in dp:
    print(i)