# 수 묶기
# 백준 #1744 : 수 묶기
'''https://www.acmicpc.net/problem/1744'''

import sys

try:
    n = int(sys.stdin.readline())
    numbers = [int(sys.stdin.readline()) for _ in range(n)]
    result = 0
    
    numbers.sort(reverse=True)
    
    pre_number = 0
    result = 0
    zero_count = 0
    negative_start_idx = n
    
    for idx, number in enumerate(numbers):
        if number == 1:
            result += 1
        elif number == 0:
            zero_count += 1
            
        elif number < 0:
            negative_start_idx = idx
            break
        
        else:
            if pre_number == 0:
                pre_number = number
            else:
                result += pre_number * number
                pre_number = 0
            
    
    # 음수 처리
    result += pre_number
    # print(result)
    pre_number = 0
    if n - negative_start_idx >= 1:
        for idx in range(n-1,negative_start_idx-1,-1):
            if pre_number == 0:
                pre_number = numbers[idx]
            else:
                result += pre_number * numbers[idx]
                # print(idx, result)
                pre_number = 0
    
    if not zero_count:
        result += pre_number
    
    print(result)
    
except ValueError or IndexError as e:
    print(e)