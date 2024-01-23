# 용액
'''https://www.acmicpc.net/problem/2467'''

import sys


if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        solutions = list(map(int, sys.stdin.readline().split(" ")))
        
        i, j = 0, N-1
        sum_min = abs(solutions[i] + solutions[j])
        answer = i,j
        
        if solutions[i] * solutions[j] >= 0:
            answer = (0, 1) if solutions[0] >= 0 else (N-2, N-1)
            
        else:
            while i < j:
                sum_of_two_solutions = solutions[i] + solutions[j]
                if abs(sum_of_two_solutions) < sum_min:
                    sum_min = abs(sum_of_two_solutions)
                    answer = i, j
                
                if sum_of_two_solutions == 0:
                    answer = i, j
                    break
                
                if sum_of_two_solutions < 0:
                    i += 1
                    
                else:
                    j -= 1
        
        print(solutions[answer[0]], solutions[answer[1]])
        
    except ValueError or IndexError as e:
        print(e)