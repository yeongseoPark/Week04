# 그리디 (하) - 잃어버인 괄호

import sys, re

# n = str(sys.stdin.readline())

# split_n = re.findall(r'\d+|[+\-*/]', n)

# for i in split_n:
#    split_n[i] = split_n.lstrip('0')

# for i in range(len(split_n)):
#     if len(split_n) >= 5:
#       if split_n[i]== '-':
#         if split_n[i+2] =='+':
#             split_n =  split_n[:i+1] + ['('] + split_n[i+1:i+4] +[')'] 


# n= ' '.join(split_n)

# print(eval(n))



string = sys.stdin.readline().split('-')
s = 0

for i in string[0].split('+'):
    s += int(i)
    
for i in string[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)