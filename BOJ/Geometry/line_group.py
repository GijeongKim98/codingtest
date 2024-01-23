# 선분 그룹
'''https://www.acmicpc.net/problem/2162'''

import sys

def is_cross(l1, l2):
    p1, p2 = (l1[0],l1[1]),(l1[2],l1[3])
    p3, p4 = (l2[0],l2[1]),(l2[2],l2[3])
    
    ccw1, ccw2, ccw3, ccw4 = ccw(p1,p2,p3), ccw(p1,p2,p4), ccw(p3,p4,p1), ccw(p3,p4,p2)

    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        if p1[0] == p2[0]:
            if p1[1] > p2[1]:
                p1, p2 = p2, p1
            if p3[1] > p4[1]:
                p3, p4 = p4, p3
                
            if p1[1] > p4[1]:
                if p2[1] < p3[1]:
                    return True
                else:
                    return False
            
            if p2[1] < p3[1]:
                return False
            else:
                return True
        else:
            if p1[0] > p2[0]:
                p1, p2 = p2, p1
            if p3[0] > p4[0]:
                p3, p4 = p4, p3
            
            if p1[0] > p4[0]:
                if p2[0] < p3[0]:
                    return True
                else:
                    return False
            
            if p2[0] < p3[0]:
                return False
            else:
                return True
            
    condition1 = ccw1 * ccw2
    condition2 = ccw3 * ccw4
    
    if condition1 > 0 or condition2 > 0:
        return False
       
    return True


def ccw(p,q,r):
    c_p = cross_product(vector(p,q), vector(p,r))
    
    if c_p == 0:
        return 0
    else:
        return -1 if c_p < 0 else 1
    

def vector(p1,p2):
    return p2[0] - p1[0], p2[1] - p1[1]


def cross_product(v, u):
    return v[0] * u[1] - v[1] * u[0]


def find(x):
    if x == root[x]:
        return x
    
    root[x] = find(root[x])
    
    return root[x]


def union(x,y):
    global count_of_group
    x, y = find(x), find(y)
    
    if x == y:
        return
    
    if rank[x] > rank[y]:
        x, y = y, x
        
    root[y] = x
    rank[x] += rank[y]
    
    count_of_group -= 1
    

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        lines = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        root = [line for line in range(N+1)]
        rank = [1 for line in range(N+1)]
        count_of_group = N
        
        for idx1 in range(N-1):
            for idx2 in range(idx1+1, N):
                if is_cross(lines[idx1], lines[idx2]):
                    union(idx1, idx2)
                    
        print(f"{count_of_group}\n{max(rank)}")
                    
    except ValueError or IndexError or ZeroDivisionError as e:
        print(e)