# 도시 분할 계획
'''https://www.acmicpc.net/problem/1647'''

import sys

def find(x):
    if x == root[x]:
        return x
    else:
        return find(root[x])
    
def union(x,y):
    x, y = find(x), find(y)
    
    if x == y:
        return False
    
    if rank[x] < rank[y]:
        x, y = y, x
    
    root[y] = x
    
    if rank[x] == rank[y]:
        rank[x] += 1
    
    return True
    
    


if __name__ == "__main__":
    try:
        N, M = map(int, sys.stdin.readline().split(" "))
        edges = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(M)]

        # sort edges
        edges.sort(key=lambda x: x[2])
        
        # cost_list
        cost_list = []
        
        # Rank : 트리의 높이 
        rank = [0 for _ in range(N+1)]
        
        # Root
        root = [node for node in range(N+1)]
        
        for x, y, c in edges:
            bool_ = union(x,y)
            if bool_:
                cost_list.append(c)
        
        print(sum(cost_list[:-1]))
        
    except ValueError or IndexError as e:
        print(e)
    
        
