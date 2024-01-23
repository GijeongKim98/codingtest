# 사이클 게임
'''https://www.acmicpc.net/problem/20040'''

import sys

def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])
    
    return root[x]

def union(x, y):
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
        n, m = map(int, sys.stdin.readline().split(" "))
        lines = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(m)]
        
        answer = 0
        rank = [0 for _ in range(n)]
        root = [i for i in range(n)]
        
        
        for idx, (x, y) in enumerate(lines, start=1):
            if not union(x,y):
                answer = idx
                break
        
        print(answer)
        
    except ValueError or IndexError as e:
        print(e)