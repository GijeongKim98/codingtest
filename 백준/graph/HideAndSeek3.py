# 숨바꼭질3
'''https://www.acmicpc.net/problem/13549'''

from collections import deque
import sys

try:
    N, K = map(int, sys.stdin.readline().split(" "))
    
    if K <= N:
        print(N - K)
    
    else:
        result = K - N + 1
        min_value = K+result
        visited = [0 for _ in range(min_value)]
        
        queue = deque([N])
        visited[N] = 1
        
        while queue:
            
            pop = queue.popleft()
            
            if pop == K:
                result = min(visited[pop], result)
            
            if pop > K: 
                if not visited[pop-1]:
                    visited[pop-1] = visited[pop] + 1
                    queue.append(pop-1)
                continue
            
            new_node = pop * 2
            if 0 <= new_node and new_node < min_value and not visited[new_node]:
                    visited[new_node] = visited[pop]
                    queue.append(new_node)
            
            new_nodes = [pop-1, pop+1]
            
            for new_node in new_nodes:
                if 0 <= new_node and new_node < min_value and not visited[new_node]:
                    visited[new_node] = visited[pop] + 1
                    queue.append(new_node)
                    
                
        print(result - 1)

except ValueError or IndexError as e:
    print(e)