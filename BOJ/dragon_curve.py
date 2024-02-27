# 드래곤 커브
'''https://www.acmicpc.net/problem/15685'''


import sys

directions = [(1,0), (0,-1), (-1,0), (0,1)]

def get_next_curve_points(points, sx, sy):
    new_points = points[:]
    
    len_p = len(points)
    
    for x, y in points:
        if sx != x or sy != y:
            rx, ry = -y+sx+sy, x-sx+sy
            new_points.append((rx,ry))

    return new_points, new_points[len_p][0], new_points[len_p][1]
        

def search_point(x,y,d,g):
    points = [(x,y), (x+directions[d][0], y+directions[d][1])]
    if g == 0:
        return points
    
    sx, sy = x+directions[d][0], y+directions[d][1]

    for _ in range(g):
        points, sx, sy = get_next_curve_points(points, sx, sy)
        
    return list(set(points))
        
        
        
if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        
        graph = [set() for _ in range(101)]
        
        for _ in range(N):
            sx, sy, d, g = map(int, sys.stdin.readline().split(" "))
            points = search_point(sx,sy,d,g)
            
            for x, y in points:
                if y < 0 or x < 0:
                    print("Value Error : dragon curve out of range 0 100")
                    sys.exit()
                graph[y].add(x)
        
        answer = 0
        
        list_ = list(graph[0])
        for y in range(1, 101):
            for x in list_:
                if (x+1) in graph[y-1] and (x+1) in graph[y] and x in graph[y]:
                    answer += 1
            
            list_ = list(graph[y])
        
        print(answer)    

    except ValueError or IndexError as e:
        print(e)
         
