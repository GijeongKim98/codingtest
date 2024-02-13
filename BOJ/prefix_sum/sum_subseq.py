# 부분합
"""https://www.acmicpc.net/problem/1806"""

import sys

INF = 1_000_000

def search(s):
    prefix_sum = [0]
    sum_ = 0
    min_length = INF
    
    for num in numbers:
        sum_ += num
        prefix_sum.append(sum_)
        if num >= s:
            return 1
    
    start_idx = 0
    for end_idx, sum_ in enumerate(prefix_sum[1:], start=1):
        while sum_ - prefix_sum[start_idx] >= s:
            min_length = min(end_idx-start_idx, min_length)
            start_idx += 1 
            
    return min_length if min_length != INF else 0
        

if __name__ == "__main__":
    try:
        N, S = map(int, sys.stdin.readline().split(" "))
        numbers = list(map(int, sys.stdin.readline().split(" ")))
        
        answer = search(S) 
        print(answer)   
        
    
    except ValueError or IndexError as e:
        print(e)