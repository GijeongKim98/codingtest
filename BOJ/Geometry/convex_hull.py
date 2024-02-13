# 블록 껍질
'''https://www.acmicpc.net/problem/1708'''

# Method : 그라함 스캔 알고리즘

import sys

# 각도 구하는 알고리즘
# 실제 각도가 아닌 dx가 0이 되는 것을 방지하기 위함
def theta(a, b):
    xa, ya = points[a]
    xb, yb = points[b]
    
    dx, dy = xb - xa, yb - ya
    ax, ay = abs(dx), abs(dy)
    
    dist = ax + ay
    
    if ax + ay == 0:
        t = 0
    else:
        t = dy / (ax + ay)
    
    if dx < 0:
        return 2 - t, dist
    elif dy < 0:
        return 4 + t, dist
    else:
        return t, dist
    
# CCW 알고리즘 : 벡터의 외적에서 방향을 확인
def ccw(i, j, k):
    (vx1, vy1), (vx2, vy2) = vector(i, j), vector(j, k)
    product_value = vx1 * vy2 - vy1 * vx2
    return True if product_value > 0 else False    


# vector 생성 함수
def vector(idx1, idx2): # 1 -> 2로 가는 벡터 생성
    (x1, y1), (x2, y2) = points[idx1], points[idx2] 
    return x2 - x1, y2 - y1

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        points = [tuple(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        standard_point = 0
        
        for idx, (x, y) in enumerate(points[1:], start=1):
            if points[standard_point][1] > y:
                standard_point = idx
            elif points[standard_point][1] == y and points[standard_point][0] < x:
                standard_point = idx
                
        
        theta_list = [[i,10,0] for i in range(N)]
        
        for idx in range(N):
            theta_, dist_ = theta(standard_point, idx)
            theta_list[idx][1], theta_list[idx][2] = theta_, dist_
            
            
            
        theta_list.sort(key=lambda x: (x[1], x[2]))
        
        stack = []
        
        for idx, (p, _, _) in enumerate(theta_list):
            if p == standard_point:
                theta_list[0], theta_list[idx] = theta_list[idx], theta_list[0]
        
        for p, _, _ in theta_list:
            # if p == standard_point:
            #     continue
            
            while len(stack) > 1 and not ccw(stack[-2], stack[-1], p):
                stack.pop()
            
            stack.append(p)
        
        while len(stack) > 1 and not ccw(stack[-2], stack[-1], standard_point):
            stack.pop()    
        
        print(len(stack))
                    
    except ValueError or IndexError as e:
        print(e)