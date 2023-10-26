# 음악프로그램
'''https://www.acmicpc.net/problem/2623'''

import sys
from collections import deque

if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        orders = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        graph = {i: dict() for i in range(1, N+1)}
        in_degree_list = [0 for _ in range(N+1)]
        
        for order in orders:
            pre_x = order[1]
            for new_x in order[2:]:
                if new_x in graph[pre_x]:
                    graph[pre_x][new_x] += 1
                else:
                    graph[pre_x][new_x] = 1
                
                pre_x = new_x                
                in_degree_list[new_x] += 1

        start_node = []
        
        for singer in range(1,N+1):
            if not in_degree_list[singer]:
                start_node.append(singer)
        
        queue = deque(start_node)
        answer = []
        
        while queue:
            pop = queue.popleft()
            answer.append(pop)
            for new in graph[pop]:
                in_degree_list[new] -= graph[pop][new]
                if not in_degree_list[new]:
                    queue.append(new)
                    
            # print(f"queue = {queue} // pop = {pop}")
                    
        if len(answer) != N:
            print(0)
        else:
            for a in answer:
                print(a)
        
    except ValueError or IndexError as e:
        print(e)
        