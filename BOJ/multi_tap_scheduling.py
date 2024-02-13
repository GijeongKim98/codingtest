# 멀티탭 스케줄링
'''https://www.acmicpc.net/problem/1700'''


import sys

def find(now):
    max_order = now
    max_idx = 0
    for idx, item in enumerate(item_list):
        try:
            next_order = order[now:].index(item) + now
        except ValueError:
            return idx

        if max_order < next_order:
            max_order = next_order
            max_idx = idx
    
    return max_idx




if __name__ == "__main__":
    try:
        N, K = map(int,sys.stdin.readline().split(" "))
        order = list(map(int,sys.stdin.readline().split(" ")))
        
        answer = 0

        item_set = set()
        item_list = list()

        for now, item in enumerate(order):
            if item not in item_set:
                if len(item_list) == N:
                    d_idx = find(now)
                    item_set -= {item_list[d_idx]}
                    item_list[d_idx] = item
                    answer += 1
                    
                else:
                    item_list.append(item)
                
                item_set.add(item)

        print(answer)

    except ValueError or IndexError as e:
        print(e)