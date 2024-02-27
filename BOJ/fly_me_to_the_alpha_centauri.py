# Fly me to the Alpha Centauri
'''https://www.acmicpc.net/problem/1011'''

import sys
import math

def solution(dist):
    if dist == 1:
        return 1
    
    n = int((math.sqrt(1+4*dist) - 1) / 2)
    
    r = dist - (n * (n+1))
    
    if r > n+1:
        return n*2 + 2
    
    elif r == 0:
        return n*2
    
    else:
        return n*2 + 1
    

if __name__ == "__main__":
    try:
        C = int(sys.stdin.readline())
        
        for _ in range(C):
            x, y = map(int, sys.stdin.readline().split(" "))
            print(solution(y-x))
        
    except ValueError as e:
        print(e)