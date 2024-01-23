# 수 나누기 게임
'''https://www.acmicpc.net/problem/27172'''

import sys

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        numbers = list(map(int, sys.stdin.readline().split(" ")))
        
        num2idx = {num : idx for idx, num in enumerate(numbers)}
        
        set_of_nums = set(numbers)
        
        numbers.sort()
        
        max_ = numbers[-1]
        
        answer = [0 for _ in range(N)]
        
        for number in numbers:
            for num in range(number, max_+1, number):
                if num in set_of_nums:
                    answer[num2idx[number]] += 1
                    answer[num2idx[num]] -= 1
        
        print(*answer)
                    
               
    except ValueError or IndexError as e:
        print(e)