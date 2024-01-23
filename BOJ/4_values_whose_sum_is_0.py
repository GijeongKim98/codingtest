# 합이 0인 네 정수
'''https://www.acmicpc.net/problem/7453'''

import sys

A, B, C, D = 0,1,2,3

# def binary_search(s):
#     low, high = 0, len(sum_numbers_C_D) - 1 
#     while low <= high:
#         mid = (low + high) // 2
        
#         if sum_numbers_C_D[mid] < s:
#             low = mid + 1
#         elif sum_numbers_C_D[mid] > s:
#             high = mid - 1
#         else:
#             return dicts[0][-1*s] * dicts[1][sum_numbers_C_D[mid]]
        
#     return 0
    
    


if __name__ == "__main__":
    try:
        n = int(sys.stdin.readline())
        numbers = [[] for _ in range(4)]
        
        for _ in range(n):
            number_list = list(map(int, sys.stdin.readline().split(" ")))
            for idx, number in enumerate(number_list):
                numbers[idx].append(number)
        
        dicts = [dict(), dict()]
        sum_ab = []
        sum_cd = dict()
        
        for i in range(n):
            for j in range(n):
                sum_ab.append(numbers[0][i] + numbers[1][j])
                sum_ = numbers[2][i] + numbers[3][j]
                if sum_ in sum_cd:
                    sum_cd[sum_] += 1
                else:
                    sum_cd[sum_] = 1
        
        # sum_numbers_C_D = list(dicts[1].keys())
        # sum_numbers_C_D.sort()
        
        answer = 0
        
        a = 0
        
        for num in sum_ab:
            answer += sum_cd.get(-num,0)
            
            # for num2 in sum_numbers_C_D:
            #     if num + num2 == 0:
            #         print(f"number 1 = {num} // number 2 = {num2}")
            #         a += 1
                    
        
            
        
        print(answer)
        
        # print(f'a : {a}')
        
    except ValueError or IndexError as e:
        print(e)