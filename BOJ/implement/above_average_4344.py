# 백준 4344번 : 평균은 넘겠지
'''https://www.acmicpc.net/problem/4344'''

import sys

try:
    number_of_testcase = int(sys.stdin.readline())
    for _ in range(number_of_testcase):
        N, *scores = map(int, sys.stdin.readline().split(" "))
        average_of_scores = sum(scores) / N
        count = 0
        for score in scores:
            if score > average_of_scores:
                count += 1
                
        print(f"{round((count*100)/N, 3):.3f}%")
        
except ValueError or IndexError as e:
    print(e)