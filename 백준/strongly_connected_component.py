# Strongly Connected Component
'''https://www.acmicpc.net/problem/2150'''

import sys
sys.setrecursionlimit(10001)

def dfs(node): 
    parents[0] += 1
    parent = parents[node] = parents[0]
    stack.append(node)
    
    for connected_node in graph[node]:
        if not parents[connected_node]:
            parent = min(parent, dfs(connected_node))
        elif not finished[connected_node]:
            parent = min(parents[connected_node], parent)
    
    if parents[node] == parent:
        scc_set = []
        while stack:
            pop = stack.pop()
            finished[pop] = True
            scc_set.append(pop)
            if parents[pop] == parent:
                break
        
        answer.append(scc_set)
    
    return parent
                
        
    
if __name__ == "__main__":
    try:
        V, E = map(int, sys.stdin.readline().split(" "))
        graph = {i : [] for i in range(1,V+1)}
        
        for _ in range(E):
            x, y = map(int, sys.stdin.readline().split(" "))
            graph[x].append(y)
        
        # visited = [0 for _ in range(V+1)]
        
        parents = [0 for _ in range(V+1)]
        finished = [False for _ in range(V+1)]
        stack = []
        answer = []
        
        for node in range(1, V+1):
            if not parents[node]:
                dfs(node)
        
        for i in range(len(answer)):
            answer[i].sort()
            answer[i].append(-1)
            
        answer.sort(key=lambda x : x[0])
        
        print(len(answer))
        
        for a in answer:
            print(*a, sep=" ")
            
                
    except ValueError or IndexError as e:
        print(e)