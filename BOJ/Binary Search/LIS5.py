# 가장 긴 증가하는 부분수열 5
'''https://www.acmicpc.net/problem/14003'''

import sys

def binary_search(number):
    low, high = 0, len(lis_list)
    
    while low < high:
        mid = (low + high) // 2
        
        if lis_list[mid] < number:
            low = mid+1
        
        elif lis_list[mid] == number:
            return mid
        
        else:
            high = mid
            
    return low


if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        numbers = list(map(int, sys.stdin.readline().split(" ")))
        
        lis_order_list = [0 for _ in range(N)]
        lis_list = [numbers[0]]
        max_length_of_lis_idx = 0 # 최대 길이를 가지는 LIS의 마지막 숫자 idx 정보
        
        # bs 성능 확인 테스트
        # lis_list = [1,3,5,7,9]
        # print(binary_search(6))
        
        for idx, number in enumerate(numbers[1:], start=1):
            if lis_list[-1] < number:
                lis_list.append(number)
                lis_order_list[idx] = len(lis_list)-1
                max_length_of_lis_idx = idx
            
            elif lis_list[-1] == number:
                lis_order_list[idx] = len(lis_list)-1
            
            else:
                search_idx = binary_search(number)
                lis_list[search_idx] = number
                lis_order_list[idx] = search_idx
        
        # 길이 및 저장된 배열 확인
        # print(len(lis_list))
        # print(lis_order_list)
        # print(max_length_of_lis_idx)
        
        lis_list[-1] = numbers[max_length_of_lis_idx]
        lis_idx = lis_order_list[max_length_of_lis_idx] - 1
        
        for idx in range(max_length_of_lis_idx-1, -1, -1):
            if lis_order_list[idx] == lis_idx:
                lis_list[lis_idx] = numbers[idx]
                lis_idx -= 1
            
            if lis_idx < 0:
                break
            
        print(len(lis_list))
        print(*lis_list, sep=" ")
           
    except ValueError or IndexError as e:
        print(e)