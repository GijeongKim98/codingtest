# 크게 만들기
'''https://www.acmicpc.net/problem/2812'''

import sys
from collections import deque

if __name__ == "__main__":
    try:
        N, K = map(int, sys.stdin.readline().split(" "))
        numbers = list(map(int, list(sys.stdin.readline().rstrip())))

        stack = deque()

        for number in numbers:
            while K > 0 and stack and stack[-1] < number:
                stack.pop()
                K -= 1
            
            stack.append(number)

        while K > 0 and stack:
            stack.pop()
            K -= 1
            
            
        print("".join(list(map(str, stack))))
    
    except ValueError or IndexError as e:
        print(e)