# 수레 움직이기
EMPTY, RS, BS, RE, BE, WALL = 0,1,2,3,4,5

from collections import deque

dx_dy = [(0,1), (1,0), (-1,0), (0,-1)]


def solution(maze):
    
    def bfs(r,b,r_num,b_num):
        queue = deque([(r,b,r_num,b_num,0)])
        
        while queue:
            pr, pb, pr_num, pb_num, pcount = queue.popleft()
            prx, pry = pr
            pbx, pby = pb
            
            if maze[pry][prx] == RE and maze[pby][pbx] == BE:
                return pcount
            
            elif maze[pry][prx] == RE:
                for bdx, bdy in dx_dy:
                    nbx, nby = pbx+bdx, pby+bdy
                    if 0>nbx or nbx>=M or 0>nby or nby>=N or pb_num & (1 << (nbx+nby*M)) or maze[nby][nbx] == WALL:
                        continue
                        
                    if prx == nbx and pry == nby:
                        continue
                        
                    queue.append(((prx,pry),(nbx,nby),pr_num,pb_num | (1 << (nbx+nby*M)), pcount+1))
                continue
            
            elif maze[pby][pbx] == BE:
                for rdx, rdy in dx_dy:
                    nrx, nry = prx+rdx, pry+ rdy
                    if 0>nrx or nrx>=M or 0>nry or nry>=N or pr_num & (1 << (nrx+nry*M)) or maze[nry][nrx] == WALL:
                        continue
                        
                    if nrx == pbx and nry == pby:
                        continue
                        
                    queue.append(((nrx,nry),(pbx,pby),pr_num | (1 << (nrx+nry*M)),pb_num, pcount+1))
                continue
            
            for rdx, rdy in dx_dy:
                nrx, nry = prx+rdx, pry+rdy
                if 0>nrx or nrx>=M or 0>nry or nry>=N or pr_num & (1 << (nrx+nry*M)) or maze[nry][nrx] == WALL:
                    continue

                for bdx, bdy in dx_dy:
                    nbx, nby = pbx+bdx, pby+bdy
                    if 0>nbx or nbx>=M or 0>nby or nby>=N or pb_num & (1 << (nbx+nby*M)) or maze[nby][nbx] == WALL:
                        continue
                        
                    if (nrx == nbx and nry == nby) or (prx == nbx and pry == nby and nrx==pbx and nry==pby):
                        continue
                        
                    queue.append(((nrx,nry),(nbx,nby),pr_num | (1 << (nrx+nry*M)),pb_num | (1 << (nbx+nby*M)), pcount+1))
        
        
        
        return 0
    
    N, M = len(maze), len(maze[0])
    
    for i in range(N):
        for j in range(M):
            if maze[i][j] == RS:
                r, r_num = (j,i), (1 << (i*M+j))
            if maze[i][j] == BS:
                b, b_num = (j,i), (1 << (i*M+j))
                
    
    answer = bfs(r,b,r_num,b_num)
    
    
    return answer