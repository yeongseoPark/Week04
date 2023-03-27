import sys
input = sys.stdin.readline
n_item, weight = map(int, input().split())
items = dict()
setting = set()
for _ in range(n_item):
    # a: 물건의 무게, b: 물건의 가치
    a, b = map(int, input().split())
    items[a] = b
    setting.add(a)
# print('items : ', items)
# print(setting)
want = [0] * (weight+1)
# print(want)
for i in range(1, weight+1):
    if i in setting:
        want[i] = max(want[i], items[i])
    for item in setting:
        try:
            want[i] = max(want[i], want[i - item] + want[item])     
        except:
            continue
print(want[-1])