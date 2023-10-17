# 부분 수열의 합 2
'''https://www.acmicpc.net/problem/1208'''


import sys

def dfs(sub, sub_sum, step, sum_ = 0):
    if len(sub) == step:
        if sum_ in sub_sum:
            sub_sum[sum_] += 1
        else:
            sub_sum[sum_] = 1
        return
    
    for idx in [0,1]:
        if idx:
            dfs(sub, sub_sum, step+1 , sum_ + sub[step])
        else:
            dfs(sub, sub_sum, step+1 , sum_)
            

def binary_search(keys, sub_sum, search_num):
    l, h = 0, len(keys)-1
    
    while l <= h:        
        mid = (l+h) // 2
        
        # print(f"mid = {mid}, l = {l}, h = {h}")
        
        if keys[mid] < search_num:
            l = mid+1
        elif keys[mid] > search_num:
            h = mid-1
        else:
            return sub_sum[keys[mid]]
    
    return 0

 

try: 
    N, S = map(int, sys.stdin.readline().split(" "))

    sequence = list(map(int, sys.stdin.readline().split(" ")))
    
    sub1, sub2 = sequence[:N//2], sequence[N//2:]
    
    sub_sum1, sub_sum2 = dict(), dict()
    
    result = 0
    
    dfs(sub1, sub_sum1, 0, 0)
    dfs(sub2, sub_sum2, 0, 0)
    
    sub_sum1[0] -= 1
    sub_sum2[0] -= 1
    
    for sum_ in sub_sum1.keys():
        if sum_ == S:
            result += sub_sum1[sum_]
    
    for sum_ in sub_sum2.keys():
        if sum_ == S:
            result += sub_sum2[sum_]
    
    key_list = list(sub_sum2.keys())
    key_list.sort()
    
    for sum_ in sub_sum1.keys():
        result += sub_sum1[sum_] * binary_search(key_list, sub_sum2, S - sum_)
    
    
    print(result)
    
except ValueError or IndexError as e:
    print(e)
    
    
    

def dfs_v2(sub, sub_sum, step, sum_ = 0):
    if len(sub) == step:
        sub_sum.append(sum_)
        return
    
    for idx in [0,1]:
        if idx:
            dfs(sub, sub_sum, step+1 , sum_ + sub[step])
        else:
            dfs(sub, sub_sum, step+1 , sum_)


def binary_search_v2(sub_sum, search_number, another_sum):
    l, h = 0, len(sub_sum)-1
    
    while l <= h:        
        mid = (l+h) // 2
        
        # print(f"mid = {mid}, l = {l}, h = {h}")
        
        if sub_sum[mid] + another_sum < search_number:
            l = mid+1
        elif sub_sum[mid] + another_sum > search_number:
            h = mid-1
        else:
            rlt = 1
            mid_num = sub_sum[mid]
            i, j = 1, 1
            while mid - i >= 0 and mid_num == sub_sum[mid-i]:
                i += 1
                rlt += 1
            
            while mid + j < len(sub_sum) and mid_num == sub_sum[mid+j]:
                j += 1
                rlt += 1
            return rlt
          
        # print(f"mid = {mid}, l = {l}, h = {h}")
    
    return 0
