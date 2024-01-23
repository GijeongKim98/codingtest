# 백준 : 보석도둑 1202번

# module
# import sys

# # Define function : binary search
# def binary_search_of_bag(weight: int) -> int:
#     """Binary_Search

#     Args:
#         weight (int): weight of jewelry

#     Returns:
#         int: index of bag 
#     """
#     low ,high = 0, len(bags)-1

#     search_index = high

#     while low < high:
#         mid = (low + high) // 2
    
#         if bags[mid] < weight:
#             low = mid
#         elif bags[mid] > weight:
#             high = mid
#             search_index = mid
#         else:
#             return mid
    
#     return search_index

# try:
#     N, K = map(int, sys.stdin.readline().split(' '))

#     jewelrys = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

#     bags = [int(sys.stdin.readline()) for _ in range(K)]

#     # jewelrys sort by value, if same value then smaller than weight the first
#     jewelrys = sorted(jewelrys, key= lambda x : (x[1], -x[0]), reverse=True)

#     # bags sort 
#     bags.sort()


#     # total_value
#     total_value = 0


#     for weight, value in jewelrys:
#         if not bags or weight > bags[-1]:
#             continue
#         idx = binary_search_of_bag(weight=weight)
#         bags = bags[:idx] + bags[idx+1:]
#         total_value += value

#     print(total_value)

# except ValueError or IndexError as e:
#     print(e)


# Reference
'''https://jaimemin.tistory.com/760'''

# module
import sys
import heapq as hq

try:
    # input
    N, K = map(int, sys.stdin.readline().split(' '))
    jewelrys = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
    bags = [int(sys.stdin.readline()) for _ in range(K)]

    # sort
    jewelrys = sorted(jewelrys, key=lambda x : (x[0],x[1]))
    bags.sort()

    # Initialization HeapQ
    heapq = []

    # jewelrys index
    idx = 0

    # Result
    result = 0

    for c_k in bags:
        while idx < N and jewelrys[idx][0] <= c_k:
            hq.heappush(heapq, -jewelrys[idx][1])
            idx += 1

        if heapq:
            result -= hq.heappop(heapq)
    
    print(result)


except ValueError or IndexError as e:
    print(e)



