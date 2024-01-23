# 다각형의 면적
'''https://www.acmicpc.net/problem/2166'''

import sys
    
if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        points = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        pre_x, pre_y = points[0]
        
        answer = points[-1][0] * pre_y - points[-1][1] * pre_x
        
        for next_x, next_y in points[1:]:
            answer += pre_x * next_y - pre_y * next_x
            pre_x, pre_y = next_x, next_y
        
        answer = abs(answer) / 2
        
        print(round(answer, 1))
        
    except ValueError or IndexError as e:
        print(e)

    