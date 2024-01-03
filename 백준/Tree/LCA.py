# LCA
'''https://www.acmicpc.net/problem/11437'''

import sys
from collections import deque

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        
        graph = {node: [] for node in range(1,N+1)}
        
        edges = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(N-1)]
        
        # initialize graph
        for x, y in edges:
            graph[y].append(x)
            graph[x].append(y)
            
        root = [x for x in range(N+1)]
        rank = [0 for _ in range(N+1)]
        
        queue = deque([1])
        rank[1] = 1
        while queue:
            pop = queue.popleft()
            for new in graph[pop]:
                if not rank[new]:
                    rank[new] = rank[pop]+1
                    root[new] = pop
                    queue.append(new)
        
        M = int(sys.stdin.readline())
        questions = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]
        
        answer = []
        
        for x, y in questions:
            while rank[y] < rank[x]:
                x = root[x]
            
            while rank[x] < rank[y]:
                y = root[y]
            
            while x != y:
                x, y = root[x], root[y]
            
            answer.append(x)
            
        
        print(*answer, sep="\n")
                
    except ValueError or IndexError as e:
        print(e)