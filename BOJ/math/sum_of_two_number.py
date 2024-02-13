# 두수의 합
'''https://www.acmicpc.net/problem/3273'''

import sys

try:
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split(" ")))
    x = int(sys.stdin.readline())
    
    numbers.sort()
    
    i, j = 0, n-1
    rlt = 0
    
    while i < j:
        sum_of_two_number = numbers[i] + numbers[j]
        
        if sum_of_two_number == x:
            i, j = i+1, j-1
            rlt += 1
        
        elif sum_of_two_number < x:
            i = i + 1
        
        else:
            j = j - 1
    
    print(rlt)
        
except ValueError or IndexError as e:
    print(e)