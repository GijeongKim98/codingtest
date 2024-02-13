# ACM Craft
'''https://www.acmicpc.net/problem/1005'''

import sys
from collections import deque

try:
    t = int(sys.stdin.readline())
    result = []
    for __ in range(t):
        N, K = map(int, sys.stdin.readline().split(" "))
        nodes = [0] + list(map(int, sys.stdin.readline().split(" ")))
        graph = {i : [] for i in range(1,N+1)}
        dp_array = [0 for _ in range(N+1)]
        
        in_degree_array = [0 for node in range(N+1)]
        
        for _ in range(K):
            x, y = map(int, sys.stdin.readline().split(" "))
            graph[x].append(y)
            in_degree_array[y] += 1
        
        W = int(sys.stdin.readline())
        
        queue = deque()
        for node, in_degree in enumerate(in_degree_array):
                if not in_degree and node > 0:
                    queue.append(node)
                    dp_array[node] = nodes[node]
        
        while queue:
            pop_node = queue.popleft()
            for new_node in graph[pop_node]:
                in_degree_array[new_node] -= 1
                if not in_degree_array[new_node]:
                    queue.append(new_node)
                dp_array[new_node] = max(dp_array[new_node], dp_array[pop_node] + nodes[new_node])
        
        print(max(nodes[W], dp_array[W]))

except ValueError or IndexError as e:
    print(e)             
            
            
        
        
        
            
                 
        
        

        
    
        
    