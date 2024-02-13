# 백준 기타줄
'''https://www.acmicpc.net/problem/1049'''

import sys

INF = 10000

try:
    N, M = map(int, sys.stdin.readline().split(' '))

    min_packages_price, min_pieces_price = INF, INF
    
    for _ in range(M):
        package, piece = map(int, sys.stdin.readline().split(' '))
        min_packages_price = min(package, min_packages_price)
        min_pieces_price = min(piece, min_pieces_price)

    result = (N//6) * min(min_packages_price, min_pieces_price * 6)
    result += min(min_packages_price, min_pieces_price * (N%6))

    print(result)

except ValueError or IndexError as e:
    print(e)


    
