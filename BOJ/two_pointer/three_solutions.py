# 세 용액
'''https://www.acmicpc.net/problem/2473'''

import sys

INF = 10_000_000_000

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        solutions = list(map(int, sys.stdin.readline().split(" ")))
        
        solutions.sort()
        
        result_sum = INF
        result_idx = [0,1,2]
        break_point = 0 
        
        for idx, solution in enumerate(solutions):
            i, j = idx+1, N-1
            
            while i < j:
                sum_ = solutions[i] + solutions[j] + solution
                
                if result_sum > abs(sum_):                   
                    result_sum = abs(sum_)
                    result_idx = [idx, i, j]
                    
                    if result_sum == 0:
                        break_point = 1
                        break
                
                if sum_ < 0:
                    i += 1
                
                else:
                    j -= 1
            
            if break_point:
                break
                        
        answer = sorted(list(map(lambda x: solutions[x], result_idx)))
        print(*answer)            
            
    except ValueError or IndexError as e:
        print(e)