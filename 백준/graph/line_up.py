# 줄 세우기
'''https://www.acmicpc.net/problem/2252'''

import sys
from collections import deque

if __name__ == "__main__":
    
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        edges = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        in_degree_list = [0 for _ in range(N+1)]
        graph = {student:[] for student in range(1,N+1)}
        
        for x, y in edges:
            graph[x].append(y)
            in_degree_list[y] += 1
        
        start_nodes = []
        
        for student, in_degree in enumerate(in_degree_list[1:], start=1):
            if not in_degree:
                start_nodes.append(student)
        
        queue = deque(start_nodes)
        result = []
        
        while queue:
            pop = queue.popleft()
            result.append(pop)
            for new in graph[pop]:
                in_degree_list[new] -= 1
                if not in_degree_list[new]:
                    queue.append(new)
        
        print(*result)
    
        
    except ValueError or IndexError as e:
        print(e)