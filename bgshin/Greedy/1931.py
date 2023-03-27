# 그리디 (중) - 회의실 배정 

import sys

n = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

sorted_lst = sorted(lst, key=lambda x: x[1])

result = [sorted_lst[0][1]]
for i in range(n-1):
    if result[-1] <= sorted_lst[i+1][0]:
        result.append(sorted_lst[i+1][1])
        
if result[-1] <= sorted_lst[n-1][0]:
    result.append(sorted_lst[n-1][1])
print(len(result))

---------------------------

import sys

N = int(sys.stdin.readline())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)
