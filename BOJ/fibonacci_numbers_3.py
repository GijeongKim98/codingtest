# 피보나치 수 3
'''https://www.acmicpc.net/problem/2749'''

import sys

CONSTANT = 1000000

def scalar_product(m1, m2):
    new_matrix = [[0 for _ in range(2)] for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                new_matrix[i][j] += m1[i][k] * m2[k][j]
                new_matrix[i][j] = new_matrix[i][j] % CONSTANT

    return new_matrix

def power(m, c):
    if c == 1:
        return m

    dev = power(m, c//2)

    if c % 2 == 1:
        return scalar_product(scalar_product(dev, dev), m)
    
    return scalar_product(dev, dev)

if __name__ == "__main__":
    try:
        n = int(sys.stdin.readline())

        if n < 3:
            print(1)

        else:
            matrix = [[1,1],
                    [1,0]]
            
            answer = power(matrix, n-1)[0][0]

            print(answer)
    
    except ValueError as e:
        print(e)