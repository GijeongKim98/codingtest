# 백준  2493번 : 탑
'''https://www.acmicpc.net/problem/2493'''

import sys

try:
    # Input
    N = int(sys.stdin.readline())
    towers = list(map(int, sys.stdin.readline().split(' ')))
    
    # Initialize Stack
    stack = []
    
    result = [0 for _ in range(N)]
    
    for tower_idx in range(N-1,-1,-1):
        while stack and towers[stack[-1]] <= towers[tower_idx]:
            result[stack.pop()] = tower_idx+1
        stack.append(tower_idx)
    
    print(*result)
    
except ValueError or IndexError as e:
    print(e)