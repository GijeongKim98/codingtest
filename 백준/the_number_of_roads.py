# 길의 개수
'''https://www.acmicpc.net/problem/1533'''

import sys

CONST = 1_000_003

def init_matrix():
    for i in range(N):
        for j in range(N):
            if graph[i][j] > 0:
                matrix[i*5][j*5 + graph[i][j] - 1] = 1
        for k in range(4):
            matrix[i*5+k+1][i*5+k] = 1
            
def product_m(m1, m2):
    new_m = [[0 for _ in range(5*N)] for _ in range(5*N)]
    
    for i in range(5*N):
        for j in range(5*N):
            sum_ = 0
            for k in range(5*N):
                sum_ += m1[i][k] * m2[k][j]
                sum_ = sum_ % CONST
            
            new_m[i][j] = sum_
    return new_m
    
def power_m(m, k):
    if k == 1:
        return m
    
    div = power_m(m, k//2)
    
    if k % 2 == 0:
        return product_m(div, div)
    
    return product_m(div, product_m(div,m))
    

if __name__ == "__main__":
    try:
        N, S, E, T = map(int, sys.stdin.readline().split(" "))
        graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
        
        matrix = [[0 for _ in range(5*N)] for _ in range(5*N)]
        init_matrix()
        
        # for row in matrix:
        #     print(row)
        
        answer_m = power_m(matrix, T)
        
        # for row in answer_m:
        #     print(row)
        
        print(answer_m[5 *(S-1)][5 * (E-1)])
        
         

    except ValueError or IndexError as e:
        print(e)