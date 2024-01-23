# 별자리만들기
'''https://www.acmicpc.net/problem/4386'''

import sys
import heapq as hq
import math

def get_dist(x1,y1,x2,y2):
    return math.sqrt(abs(x1-x2) ** 2 + abs(y1-y2) ** 2)

def find(a):
    if a == root[a]:
        return a

    root[a] = find(root[a])
    
    return root[a]
    
def union(a,b):
    a, b = find(a), find(b)
    
    if a == b:
        return False
    
    if rank[a] < rank[b]:
        a, b = b, a
    
    root[b] = a
    
    if rank[a] == rank[b]:
        rank[a] += 1
        
    return True

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        stars = [tuple(map(float, sys.stdin.readline().split(" "))) for _ in range(N)]

        queue = []
        
        for i, (x, y) in enumerate(stars):
            for j in range(i+1,N):
                another_x, another_y = stars[j]
                dist = get_dist(x,y,another_x,another_y)
                hq.heappush(queue, (dist, i, j))
        
        root = [node for node in range(N)]
        rank = [0 for _ in range(N)]        
        number_of_constellation = N
        
        answer = 0
        
        while queue:
            dist, a, b = hq.heappop(queue)
            if union(a,b):
                number_of_constellation -= 1
                answer += dist
            
            if not number_of_constellation:
                break
        
        print(round(answer,2))                
        
        
    except ValueError or IndexError as e:
        print(e)