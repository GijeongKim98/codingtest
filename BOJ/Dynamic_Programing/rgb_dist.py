# RGB 거리 2
'''https://www.acmicpc.net/problem/17404'''

import sys

R, G, B = 0, 1, 2

INF = 10_000_000_000

if __name__ == "__main__":
    try:
        N = int(sys.stdin.readline())
        buildings = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
        
        init_idx = [R, G, B]
        
        costs = [buildings[0][R],buildings[0][G],buildings[0][B]]
        
        for i in range(1, N-1):
            r, g, b = buildings[i]
            if costs[R] > costs[G]:
                b_idx = init_idx[G]
                b += costs[G]
            else:
                b_idx = init_idx[R]
                b += costs[R]

            if costs[G] > costs[B]:
                r_idx = init_idx[B]
                r += costs[B]
            else:
                r_idx = init_idx[G]
                r += costs[G]
            
            if costs[B] > costs[R]:
                g_idx = init_idx[R]
                g += costs[R]
            else:
                g_idx = init_idx[B]
                g += costs[B]

            init_idx = [r_idx, g_idx, b_idx]
            costs = [r,g,b]
    
        r, g, b = buildings[-1]
        
        if init_idx[G] == R and init_idx[B] == R:
            r = INF
        elif init_idx[G] == R:
            r += costs[B]
        elif init_idx[B] == R:
            r += costs[G]
        else:
            r += min(costs[B], costs[G])
        
        if init_idx[B] == G and init_idx[B] == G:
            g = INF
        elif init_idx[B] == G:
            g += costs[R]
        elif init_idx[R] == G:
            g += costs[B]
        else:
            g += min(costs[R], costs[B])
        
        if init_idx[R] == B and init_idx[G] == B:
            b = INF
        elif init_idx[R] == B:
            b += costs[G]
        elif init_idx[G] == B:
            b += costs[R]
        else:
            b += min(costs[R], costs[G])
        
        min_ = min(r,g,b)
        
        # print(min_)
        
        init_idx = [R, G, B]
        
        costs = [buildings[-1][R],buildings[-1][G],buildings[-1][B]]
        
        for i in range(N-2, 0, -1):
            r, g, b = buildings[i]
            if costs[R] > costs[G]:
                b_idx = init_idx[G]
                b += costs[G]
            else:
                b_idx = init_idx[R]
                b += costs[R]

            if costs[G] > costs[B]:
                r_idx = init_idx[B]
                r += costs[B]
            else:
                r_idx = init_idx[G]
                r += costs[G]
            
            if costs[B] > costs[R]:
                g_idx = init_idx[R]
                g += costs[R]
            else:
                g_idx = init_idx[B]
                g += costs[B]

            init_idx = [r_idx, g_idx, b_idx]
            costs = [r,g,b]
    
        r, g, b = buildings[0]

        if init_idx[G] == R and init_idx[B] == R:
            r = INF
        elif init_idx[G] == R:
            r += costs[B]
        elif init_idx[B] == R:
            r += costs[G]
        else:
            r += min(costs[B], costs[G])
        
        if init_idx[B] == G and init_idx[B] == G:
            g = INF
        elif init_idx[B] == G:
            g += costs[R]
        elif init_idx[R] == G:
            g += costs[B]
        else:
            g += min(costs[R], costs[B])
        
        if init_idx[R] == B and init_idx[G] == B:
            b = INF
        elif init_idx[R] == B:
            b += costs[G]
        elif init_idx[G] == B:
            b += costs[R]
        else:
            b += min(costs[R], costs[G])
        4
        min_ = min(r,g,b, min_)
        
        print(min_)

    except ValueError or IndexError as e:
        print(e)