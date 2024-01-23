# 가장 긴 증가하는 부분 수열
'''https://www.acmicpc.net/problem/11053'''

try:
    N = int(input())
    numbers = list(map(int, input().split(' ')))
    dp_arr = [1] * N
    rlt = 0
    for i, number in enumerate(numbers):
        max_ = 0
        for j in range(i):
            if number > numbers[j]:
                max_ = (max_ if max_ > dp_arr[j] else dp_arr[j])
        dp_arr[i] = max_ + 1

        if dp_arr[i] > rlt:
            rlt = dp_arr[i]
    
    print(rlt)
except ValueError or IndexError:
    print("Input Error")