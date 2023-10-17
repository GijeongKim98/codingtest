# 두 배열의 합
'''https://www.acmicpc.net/problem/2143'''

import sys

def binary_search(sum_list, search_number):
    low, high = 0, len(sum_list)-1
    
    while low <= high:
        mid = (low + high) // 2
        
        if sum_list[mid] < search_number:
            low = mid + 1
        
        elif sum_list[mid] > search_number:
            high = mid - 1
        
        else:
            return True
    
    return False

def search_sub_list_sum(array):
    prefix_sum = [0]
    sum_ = 0
    dictionary = dict()
    
    for number in array:
        sum_ += number
        prefix_sum.append(sum_)

    for e_idx, pre_sum in enumerate(prefix_sum[1:], start=1):
        for s_idx in range(e_idx):
            sum_s_e = pre_sum - prefix_sum[s_idx]
            if sum_s_e in dictionary:
                dictionary[sum_s_e] += 1
            else:
                dictionary[sum_s_e] = 1
    
    return dictionary

if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline())
        len_A = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split(" ")))
        len_B = int(sys.stdin.readline())
        B = list(map(int, sys.stdin.readline().split(" ")))
        
        sum_A = search_sub_list_sum(A)
        sum_B = search_sub_list_sum(B)
        
        sum_A_keys = list(sum_A.keys())
        sum_A_keys.sort()
        
        answer = 0
        
        for sum_b in sum_B:
            is_searching_num = binary_search(sum_list=sum_A_keys, search_number=T-sum_b)
            if is_searching_num:
                answer += sum_A[T-sum_b] * sum_B[sum_b]
        
        print(answer)

    except ValueError or IndexError as e:
        print(e)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn