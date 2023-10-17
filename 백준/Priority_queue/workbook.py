# 문제집
'''https://www.acmicpc.net/problem/1766'''

# Method 1 : 우선순위 큐

import sys
import heapq as hq

if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        promblems_info = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        graph = {problem : [] for problem in range(1,N+1)}
        
        in_degree_list = [0 for _ in range(N+1)]
        
        for pre, pro in promblems_info:
            graph[pre].append(pro)
            in_degree_list[pro] += 1
        
        queue = []
        
        for problem, degree in enumerate(in_degree_list[1:], start=1):
            if not degree:
                hq.heappush(queue, problem)
                
                
        result = []
        
        while queue:
            pop_ = hq.heappop(queue)
            result.append(pop_)
            for new_ in graph[pop_]:
                in_degree_list[new_] -= 1
                if not in_degree_list[new_]:
                    hq.heappush(queue,new_)
        
        print(" ".join(list(map(str, result))))
            
    
    except ValueError or IndexError as e:
        print(e)