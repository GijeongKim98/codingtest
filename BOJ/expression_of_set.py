## 집합의 표현
'''https://www.acmicpc.net/problem/1717'''

import sys

def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])
    
    return root[x]


def union(x, y):
    x, y = find(x), find(y)
    
    if x == y:
        return
    
    if rank[x] < rank[y]:
        x, y = y, x
        
    root[y] = x
    
    if rank[x] == rank[y]:
        rank[x] += 1
    
    
    return 

if __name__ == "__main__":
    try:
        n, m = map(int,sys.stdin.readline().split(" "))

        root = [x for x in range(n+1)]
        rank = [0 for _ in range(n+1)]
        
        result = []
        
        for _ in range(m):
            c, x, y = map(int, sys.stdin.readline().split(" "))
            
            if c == 0:
                union(x,y)
            
            else:
                result.append(1 if find(x) == find(y) else 0)
                
        
        for r in result:
            print("YES" if r else "NO")
        
        
    except ValueError or IndexError as e:
        print(e)