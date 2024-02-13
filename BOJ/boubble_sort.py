# 버블 소트
'''https://www.acmicpc.net/problem/1517'''

import sys

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    
    arr = merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

    return arr
    

def merge(left, right):
    global answer
    merge_list = []

    l_idx, r_idx = 0, 0

    count = 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            merge_list.append(left[l_idx])
            l_idx += 1
            answer += count
        else:
            merge_list.append(right[r_idx])
            r_idx += 1
            count += 1
        
    while l_idx < len(left):
        merge_list.append(left[l_idx])
        l_idx += 1
        answer += count
    
    while r_idx < len(right):
        merge_list.append(right[r_idx])
        r_idx += 1

    
    return merge_list


if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        numbers = list(map(int, sys.stdin.readline().split(" ")))

        answer = 0

        merge_sort(numbers)

        print(answer)



    except ValueError or IndexError as e:
        print(e)