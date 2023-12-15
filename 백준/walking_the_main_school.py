# 본대 산책
'''https://www.acmicpc.net/problem/12850'''

MATRIX = [[0,1,0,0,0,1,0,0],
          [1,0,1,0,0,1,0,0],
          [0,1,0,1,0,1,1,0],
          [0,0,1,0,1,0,1,0],
          [0,0,0,1,0,0,0,1],
          [1,1,1,0,0,0,1,0],
          [0,0,1,1,0,1,0,1],
          [0,0,0,0,1,0,1,0],]


CONST = 1_000_000_007
LEN = 8

def scalar_product(m1, m2):
    new_m = [[0 for _ in range(LEN)] for _ in range(LEN)]
    for i in range(LEN):
        for j in range(LEN):
            sum_ = 0
            for k in range(LEN):
                sum_ += m1[i][k] * m2[k][j]
                sum_ %= CONST
            
            new_m[i][j] = sum_
    
    return new_m

def power(m, c):
    if c == 1:
        return m
    div = power(m,c//2)
    
    if c % 2 == 0:
        return scalar_product(div, div)
    
    return scalar_product(div, scalar_product(m, div))



if __name__ =="__main__":
    try:
        D = int(input())
        
        matrix = power(MATRIX,D)
        
        print(matrix[0][0])
    
    except ValueError or IndexError as e:
        print(e)