n = str(input()).split('-') # -를 기준으로 괄호치기 위해서 -로 끊어줌
num = []
for i in n:
    cnt = 0 
    s = i.split('+') # 만약에 50 + 40 같은 경우면 50, 40으로 끊어주고 cnt를 통해 더한 값 저장
    for j in s:
        cnt += int(j)
    num.append(cnt)

number = num[0]
for i in range(1, len(num)):
    number -= num[i]

print(number)