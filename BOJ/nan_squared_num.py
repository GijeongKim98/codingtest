# 제곱 ㄴㄴ 수
'''https://acmicpc.net/problem/1016'''

import sys
import math

def get_squared_prime_numbers(n):
    max_ = int(math.sqrt(n))
    numbers = [True for _ in range(max_+1)]
    
    for x in range(2, max_+1):
        if not numbers[x]:
            continue
        
        for kx in range(2*x, max_+1, x):
            numbers[kx] = False
    
    sp_nums = []
    
    for x in range(2, max_+1):
        if numbers[x]:
            sp_nums.append(x*x)

    return sp_nums

if __name__ == "__main__":
    try:
        MIN, MAX = map(int, sys.stdin.readline().split(" "))
        
        # get squard prime number 
        # method : sieve of Eratosthenes
        squared_prime_numbers = get_squared_prime_numbers(MAX)
        
        # total numbers 
        # idx : MIN - MIN ~ MAX - MIN
        numbers = [1 for number in range(MAX-MIN+1)]
        
        # get nan squared numbers
        for x in squared_prime_numbers:
            start = MIN - MIN%x + x if MIN%x != 0 else MIN
            # if start > MAX:
            #     break
            for kx in range(start, MAX+1, x):
                numbers[kx - MIN] = 0
        
        answer = sum(numbers)
        
        print(answer)
        
    except ValueError or IndexError as e:
        print(e)
    