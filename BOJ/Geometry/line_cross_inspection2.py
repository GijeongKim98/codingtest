# 선분 교차2
'''https://www.acmicpc.net/problem/17387'''

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

if __name__ == "__main__":
    try:
        l1, l2 = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(2)]
        
        print(1 if is_cross(l1,l2) else 0)
        
    except ValueError or IndexError as e:
        print(e)