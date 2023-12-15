# 행성 터널
'''https://www.acmicpc.net/problem/2887'''

import sys
import heapq as hq

def find(a):
    if a == root[a]:
        return a
    
    root[a] = find(root[a])
    
    return root[a]

def union(a, b):
    a, b = find(a), find(b)
    
    if a == b:
        return 0
    
    if rank[a] < rank[b]:
        a, b = b, a
    
    root[b] = a
    
    if rank[a] == rank[b]:
        rank[a] += 1
    
    return 1
    
    

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        planets_x, planets_y, planets_z = [],[],[]
        
        for idx in range(N):
            x, y, z = map(int, sys.stdin.readline().split(" "))
            
            planets_x.append((x,idx))
            planets_y.append((y,idx))
            planets_z.append((z,idx))
        
        planets_x.sort(key=lambda x: x[0])
        planets_y.sort(key=lambda x: x[0])
        planets_z.sort(key=lambda x: x[0])
        
        queue = []
        
        pre_x, pre_y, pre_z = planets_x[0][0], planets_y[0][0], planets_z[0][0]
        pre_node1, pre_node2, pre_node3 = planets_x[0][1], planets_y[0][1], planets_z[0][1]
        
        for (x,node1), (y, node2), (z, node3) in zip(planets_x[1:],planets_y[1:],planets_z[1:]):
            abs_x, abs_y, abs_z = abs(pre_x-x), abs(pre_y-y), abs(pre_z-z)
            
            hq.heappush(queue, (abs_x,pre_node1,node1))
            hq.heappush(queue, (abs_y,pre_node2,node2))
            hq.heappush(queue, (abs_z,pre_node3,node3))
            
            pre_x, pre_y, pre_z = x, y, z
            pre_node1, pre_node2, pre_node3 = node1, node2, node3
        
        count = N
        root = [i for i in range(N)]
        rank = [0 for _ in range(N)]
        
        answer = 0
        
        while queue:
            dist, a, b = hq.heappop(queue)
            
            if union(a, b):
                answer += dist
                count -= 1
                
            
            if not count:
                break
            
        
        print(answer)
            
    except ValueError or IndexError as e:
        print(e)