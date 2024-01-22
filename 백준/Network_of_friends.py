# 친구 네트워크
'''https://www.acmicpc.net/problem/4195'''

import sys

def find(x):
    if x == root[x]:
        return x

    root[x] = find(root[x])
    
    return root[x]
    
def union(x, y):
    x, y = find(x), find(y)
    
    if x == y:
        return rank[x]
    
    if rank[x] < rank[y]:
        x, y = y, x
    
    root[y] = x
    
    rank[x] += rank[y]
    
    return rank[x]    
    
    

if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline()) 
        for _ in range(T):
            F = int(sys.stdin.readline())
            idx = 0
            
            root = []
            rank = []
            
            name2idx= dict()
            
            for _ in range(F):
                x, y = sys.stdin.readline().rstrip().split(" ")
                
                if x not in name2idx:
                    name2idx[x] = idx
                    root.append(idx)
                    rank.append(1)
                    idx += 1
                    
                if y not in name2idx:
                    name2idx[y] = idx
                    root.append(idx)
                    rank.append(1)
                    idx += 1
                
                x, y = name2idx[x], name2idx[y]
                
                c = union(x,y)
                
                print(c)
            
    except ValueError or IndexError as e:
        print(e)