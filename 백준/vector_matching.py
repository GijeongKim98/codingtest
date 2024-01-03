# 벡터 매칭
'''https://www.acmicpc.net/problem/1007'''

import sys
import math
from itertools import combinations

INF = float('inf')

def get_sum_of_vector(N, start_set):
    
    start_x, end_x, start_y, end_y = 0, 0, 0, 0

    for idx in range(N):
        x, y = points[idx]
        if idx in start_set:
            start_x += x
            start_y += y
        
        else:
            end_x += x
            end_y += y

    
    x_value, y_value = end_x - start_x, end_y - start_y

    return math.sqrt(x_value ** 2 + y_value ** 2)

    
if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            N = int(sys.stdin.readline())
            points = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
            answer = INF
            possible_lists = combinations([i for i in range(N)], N//2)

            for possible_list in possible_lists:
                set_ = set(possible_list)
                vector_sum = get_sum_of_vector(N, set_)
                answer = min(answer, vector_sum)

            print(answer)
    except ValueError or IndexError as e:
        print(e)

