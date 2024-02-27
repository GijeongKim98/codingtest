# 리모컨
'''https://www.acmicpc.net/problem/1107'''

import sys

if __name__ == "__main__":
    try:
        str_N, M = sys.stdin.readline().rstrip(), int(sys.stdin.readline())
        if M:
            broken_buttons = set(map(int, sys.stdin.readline().split(" ")))
        else:
            broken_buttons = set()
        available_buttons = set([i for i in range(10)]) - broken_buttons
        
        N = int(str_N)
        answer = abs(N - 100)
        
        if not available_buttons:
            print(answer)
        else:
            min_, max_ = min(available_buttons), max(available_buttons)
            
            numbers = list(map(int, list(str_N)))
            
            len_N = len(numbers)
            
            list_ = []
            
            for idx in range(len_N):
                if numbers[idx] in available_buttons:
                    list_.append(numbers[idx])
                else:
                    break
                
            if len(list_) == len_N:
                print(min(answer, len_N))
            
            else:
                s_count, l_count = 0, 0
                
                # small number
                small_numbers, s_idx = list_[:], idx
                while True:
                    s = numbers[s_idx] - 1
                    while s >= 0 and s in broken_buttons:
                        s -= 1
                        
                    if s == -1:
                        s_idx -= 1
                        if small_numbers:
                            small_numbers.pop()
                        else:
                            break
                        
                    else:
                        small_numbers.append(s)
                        break
                
                if s_idx == -1:
                    if len_N == 1: # small_number 가 없는 경우
                        small_number = -100
                    else: # small_number가 존재 하는데 idx = 0 자릿수 내림
                        small_number = int(str(max_)*(len_N-1))
                        s_count = len(str(small_number))
                
                else: # small_number가 존재 하는데 idx > 0
                    small_number = int("".join(list(map(str,small_numbers)))+str(max_)*(len_N-len(small_numbers)))
                    s_count = len(str(small_number))
                
                # large number
                large_numbers, l_idx = list_[:], idx
                while True:
                    l = numbers[l_idx] + 1
                    while l < 10 and l in broken_buttons:
                        l += 1
                        
                    if l == 10:
                        l_idx -= 1
                        if large_numbers:
                            large_numbers.pop()
                        else:
                            break
                        
                    else:
                        large_numbers.append(l)
                        break  
                    
                if l_idx == -1: # 자릿수를 올려야하는 경우
                    first = 1
                    while first in broken_buttons:
                        first += 1
                    
                    if first == 10: # 큰 숫자가 존재할 수 없음 버튼을 눌러 동작 x
                        large_number = 10000000
                    
                    else:
                        large_number = int(str(first) + str(min_)*(len_N))
                        l_count = len(str(large_number))
                        
                        
                else: # 일반적인 경우
                    large_number = int("".join(list(map(str,large_numbers)))+str(min_)*(len_N-len(large_numbers)))
                    l_count = len(str(large_number))
                
                s_count, l_count = s_count + abs(small_number - N), l_count + abs(large_number - N) 
                
                print(min(answer, s_count, l_count))
                
            
    except ValueError or IndexError as e:
        print(e)