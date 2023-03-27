import sys
import operator
# 넣은 후 빈도 확인하기
input = sys.stdin.readline
n_tabs, n_use = map(int, input().split())
items_order = list(map(int, input().split()))
# print(n_tabs, n_use, items_order)
# 1. set에다가 tab에 꽂아 넣기
# 2. 있으먄 뻬지 말기
# 3. 새로운 게 등장햇어 그러면 count +1 해주고 그 후에 빈도 수 높은 것을 빼지마
if n_tabs >= n_use:
    print(0)
    exit()

setting = set()
counter = 0 
### 직접짜보기
def find_latest(idx):
    result = 0
    max_idx = -1
    for num in items_order:
        try:
            num_idx = items_order[idx:].index(num)
        except:
            num_idx = n_use
        if max_idx < num_idx : 
            result, max_idx = num, num_idx
    return result

for idx, num in enumerate(items_order):
    setting.add(num)
    if len(setting) > n_tabs:
        counter += 1 
        latest_used = find_latest(idx)
        print('index', idx)
        print(setting, 'full!, to pull out: ', latest_used)
        setting.discard(latest_used)
print(counter)
