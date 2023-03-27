import sys

n = int(sys.stdin.readline())

"""
bottom-up, O(1)공간복잡도
"""
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    arr = [0,1] 
    for i in range(n-1):
        num = arr[0] + arr[1]
        arr[0], arr[1] = arr[1], arr[0]
        arr[1] = num
    
    return arr[-1]

print(fib(n))

"""
top-down, O(n)시간복잡도
"""
# fib_arr = [0] *  -> fib_arr 수열이 너무커짐
# def fib_recur(n):
#     if n < 