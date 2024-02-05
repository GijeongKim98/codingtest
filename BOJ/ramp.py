# 경사로
'''https://www.acmicpc.net/problem/14890'''

import sys
from collections import deque

def check(numbers):
    length = 0
    c = numbers[0]
    idx = 0
    while idx < N:
        number = numbers[idx]
        if c == number:
            length += 1
        
        elif c < number:
            if number - c > 1:
                return 0
            
            if length < L:
                return 0
            
            length = 1
            c = number
        
        else:
            if c - number > 1:
                return 0
            
            length = 0
            c = number

            if idx + L > N:
                return 0
        
            for j in range(idx, idx+L):
                if c != numbers[j]:
                    return 0
    
            idx += L-1

        idx += 1

    return 1



if __name__ == "__main__":
    try:
        N, L = map(int, sys.stdin.readline().split(" "))
        board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]

        answer = 0

        for i in range(N):
            high1, high2 = board[i], []
            for j in range(N):
                high2.append(board[j][i])

            answer += check(high1) + check(high2)

        print(answer)

    except ValueError or IndexError as e:
        print(e)