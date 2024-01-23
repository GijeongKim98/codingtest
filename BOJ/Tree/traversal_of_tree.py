# 트리의 순회
'''https://www.acmicpc.net/problem/2263'''

import sys
from collections import deque

sys.setrecursionlimit(10**7)


def tree_dc(i_s, i_e, p_s, p_e):
    global pre_order
    
    root = post_order_list[p_e]
    pre_order.append(root)
    
    len_r = i_e - in_order[root]
    len_l = i_e - i_s - len_r
    
    if len_l > 0:
        tree_dc(i_s, in_order[root]-1, p_s, p_e-1-len_r)
    if len_r > 0:
        tree_dc(in_order[root]+1,i_e, p_e-len_r, p_e-1)
    
    return 

if __name__ == "__main__":
    try: 
        N = int(sys.stdin.readline())
        in_order_list = list(map(int, sys.stdin.readline().split(" ")))
        post_order_list = list(map(int, sys.stdin.readline().split(" ")))
        
        in_order = dict()
        
        for idx, in_  in enumerate(in_order_list):
            in_order[in_] = idx
        
        pre_order = deque()
        
        tree_dc(0, N-1, 0, N-1)
        
        print(*pre_order)
        
    except ValueError or IndexError as e:
        print(e)