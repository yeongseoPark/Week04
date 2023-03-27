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
setting = set()
counter = 0
for i in range(1, n_use+1):
    # print(i)
    if i <= n_tabs:
        if items_order[i-1] in setting:
            continue
        else:
            setting.add(items_order[i-1])
            # print(setting)
    elif i > n_tabs:
        if items_order[i-1] in setting:
            continue
        else:
            counter_dict = dict()
            for item in setting:
                try:
                    counter_dict[item] = items_order[i-1:].count(item)
                
                except:
                    counter += 1
                    print(counter)
                    sys.exit(10)

            min_by_key = min(counter_dict.items(), key= operator.itemgetter(1))
            # print('removing', min_by_key[0])
            # print('setting', setting)
            setting.remove(min_by_key[0])
            counter += 1
            setting.add(items_order[i-1])
print(counter)                




