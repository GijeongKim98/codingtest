# 전깃줄 2
'''https://www.acmicpc.net/problem/2568'''

import sys

def binary_search(number):
    low, high = 0, len(lis)
    
    while low < high:
        mid = (low + high) // 2
        
        if lis[mid] < number:
            low = mid+1
        elif lis[mid] == number:
            return mid
        
        else:
            high = mid
    
    return low

if __name__ == "__main__":
    try:
        # Input Data
        number_of_wires = int(sys.stdin.readline())
        wires = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(number_of_wires)]
        
        # Sort for wires
        wires.sort(key=lambda x: x[1])
        
        # Search LIS
        lis_order_list = [-10 for _ in range(number_of_wires)]
        lis_order_list[0] = 0
        lis = [wires[0][0]]
        
        for idx, wire in enumerate(wires[1:], start=1):
            if lis[-1] < wire[0]:
                lis.append(wire[0])
                lis_order_list[idx] = len(lis) - 1
            
            elif lis[-1] == wire[0]:
                lis_order_list[idx] = len(lis) - 1
            
            else:
                search_idx = binary_search(wire[0])
                lis[search_idx] = wire[0]
                lis_order_list[idx] = search_idx
        
        max_length = len(lis)
        s_idx = max_length - 1
        answer = []
        
        for idx in range(number_of_wires-1, -1, -1):
            if lis_order_list[idx] == s_idx:
                s_idx -= 1
            
            else:
                answer.append(wires[idx][0])
        
        answer.sort()
        
        print(len(wires) - max_length, *answer, sep="\n")
        
        
    except ValueError or IndexError as e:
        print(e)