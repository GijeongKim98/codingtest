# 톱니바퀴
"""https://www.acmicpc.net/problem/14891"""

import sys
from collections import deque



try:
    input_list = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(4)]
    gears = {i : deque(input_list[i-1]) for i in range(1,5)}
    
    k = int(sys.stdin.readline())
    for _ in range(k):
        now, ro = map(int, sys.stdin.readline().split(" "))
        left, right = now - 1 , now + 1
        is_rotate = [0,0,0,0]
        is_rotate[now-1] = 1
        
        while left > 0 :
            if gears[left+1][6] == gears[left][2]:
                break
            is_rotate[left-1] = 1
            left -= 1
        
        while right <= 4:
            if gears[right-1][2] == gears[right][6]:
                break
            is_rotate[right-1] = 1
            right += 1
        
        if now % 2 == 1:
            s = ro
        else:
            s = ro * -1
        
        for idx, is_ro in enumerate(is_rotate, start = 1):
            if is_ro:
                gears[idx].rotate(is_ro * s)
            s *= -1

    result = 0
    mul = 1
    for key in range(1,5):
        result += gears[key][0] * mul
        mul *= 2
    
    print(result)
            
except ValueError or IndexError as e:
    print(e)