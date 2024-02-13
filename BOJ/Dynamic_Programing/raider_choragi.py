# 습격자 초라기
'''https://www.acmicpc.net/problem/1006'''
'''
import sys

RIGHT_EMPTY, LEFT_EMPTY, ALL_EMPTY, NOT_EMPTY = 0,1,2,3
RIGHT, LEFT = 1, 0


if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline())
        for _ in range(T):
            N, W = map(int, sys.stdin.readline().split(" "))
            counts = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(2)]
            list_ = [0,1,2,3]
            dp = [[0,0,0,0] for _ in range(N)]
            
            if counts[LEFT][0] + counts[RIGHT][0] <= W:
                dp[0][NOT_EMPTY] = 1
        
            if counts[LEFT][idx-1] + counts[LEFT][idx] <= W and counts[RIGHT][idx-1] + counts[RIGHT][idx] <= W:
                dp[idx][NOT_EMPTY] = 2 
                dp[0][LEFT_EMPTY] = 1
                dp[0][RIGHT_EMPTY] = 1
            
            elif counts[LEFT][idx-1] + counts[LEFT][idx] <= W:
                dp[0][RIGHT_EMPTY] = 1
        
            elif counts[RIGHT][idx-1] + counts[RIGHT][idx] <= W:
                dp[0][LEFT_EMPTY] = 1            
            
    
            for idx in range(1, N-1):
                max_ = max(dp[idx-1])
                if counts[LEFT][idx] + counts[RIGHT][idx] <= W:
                    dp[idx][NOT_EMPTY] = max_ + 1
                else:
                    dp[idx][NOT_EMPTY] = max_
                
                if counts[LEFT][idx-1] + counts[LEFT][idx] <= W and counts[RIGHT][idx-1] + counts[RIGHT][idx] <= W:
                    dp[idx][NOT_EMPTY] = max(dp[idx-1][ALL_EMPTY] + 2, dp[idx][NOT_EMPTY]) 
                    dp[idx][RIGHT_EMPTY] = dp[idx-1][LEFT_EMPTY] + 1
                    dp[idx][LEFT_EMPTY] = dp[idx-1][RIGHT_EMPTY] + 1
                    dp[idx][ALL_EMPTY] = max_
                
                elif counts[LEFT][idx-1] + counts[LEFT][idx] <= W:
                    dp[idx][RIGHT_EMPTY] = dp[idx-1][LEFT_EMPTY] + 1
                    dp[idx][LEFT_EMPTY] = max_
                    dp[idx][ALL_EMPTY] = max_
                    
                elif counts[RIGHT][idx-1] + counts[RIGHT][idx] <= W:
                    dp[idx][LEFT_EMPTY] = dp[idx-1][RIGHT_EMPTY] + 1
                    dp[idx][RIGHT_EMPTY] = max_
                    dp[idx][ALL_EMPTY] = max_
                    
                else:
                    dp[idx][LEFT_EMPTY] = max_
                    dp[idx][RIGHT_EMPTY] = max_
                    dp[idx][ALL_EMPTY] = max_
                    
            max_ = 

            if counts[LEFT][-1] + counts[RIGHT][-1] <= W:
                dp[0][NOT_EMPTY] = 1
        
            if counts[LEFT][idx-1] + counts[LEFT][idx] <= W and counts[RIGHT][idx-1] + counts[RIGHT][idx] <= W:
                dp[idx][NOT_EMPTY] = 2 
                dp[0][LEFT_EMPTY] = 1
                dp[0][RIGHT_EMPTY] = 1
            
            elif counts[LEFT][idx-1] + counts[LEFT][idx] <= W:
                dp[0][RIGHT_EMPTY] = 1
        
            elif counts[RIGHT][idx-1] + counts[RIGHT][idx] <= W:
                dp[0][LEFT_EMPTY] = 1
            
            
            
            count_group = max(dp[-1])
            print(2*N - count_group)
    except ValueError or IndexError as e:
        print(e)
'''

# 습격자 초라기

# Method 2: 
# Refer : https://blog.itcode.dev/posts/2021/06/06/a1006
# 처음과 끝에 대한 처리를 위해 배열 구조도 변경
# 처음과 끝에 대한 처리는 연산을 4번을 더해야하는 경우가 생김

import sys

UP, DOWN = 0, 1

CASE_1, CASE_2, CASE_3 = 0,1,2

def get_count_of_group(start):
    for idx in range(start, N):
        
        dp[idx][CASE_3] = dp[idx-1][CASE_3] + (1 if counts[UP][idx-1] + counts[DOWN][idx-1] <= W else 2)
        
        dp[idx][CASE_3] = min(dp[idx][CASE_3], min(dp[idx-1][CASE_2], dp[idx-1][CASE_1]) + 1)
        
        if idx > 1:
            if counts[UP][idx-2] + counts[UP][idx-1] <= W and counts[DOWN][idx-2] + counts[DOWN][idx-1] <= W:
                dp[idx][CASE_3] = min(dp[idx][CASE_3], dp[idx-2][CASE_3] + 2)

        dp[idx][CASE_1] = dp[idx][CASE_2] = dp[idx][CASE_3] + 1
        
        c = 2
        if counts[UP][idx-1] + counts[UP][idx] <= W:
            c = 1
        
        dp[idx][CASE_1] = min(dp[idx][CASE_1], dp[idx-1][CASE_2]+c)
        
        c = 2
        if counts[DOWN][idx-1] + counts[DOWN][idx] <= W:
            c = 1
            
        dp[idx][CASE_2] = min(dp[idx][CASE_2], dp[idx-1][CASE_1]+c)

if __name__ == "__main__":
    try:
        T = int(sys.stdin.readline())
        answer = []
        
        for _ in range(T):
            N, W = map(int, sys.stdin.readline().split(" "))
            counts = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(2)]
            
            dp = [[0 for _ in range(3)] for _ in range(N)]
            
            dp[0][CASE_1], dp[0][CASE_2], dp[0][CASE_3] = 1, 1, 0
            
            get_count_of_group(1)
            k = 1 if counts[UP][-1] + counts[DOWN][-1] <= W else 2
            result = min( min(dp[-1][CASE_1], dp[-1][CASE_2]) + 1, dp[-1][CASE_3]+k)
            if N > 1: 
                if counts[UP][-2] + counts[UP][-1] <= W and counts[DOWN][-2] + counts[DOWN][-1] <= W:
                    result = min(result, dp[-2][CASE_3]+2)
                
                
                if counts[UP][-1] + counts[UP][0] <= W and counts[DOWN][-1] + counts[DOWN][0] <= W:
                    dp[1][CASE_1], dp[1][CASE_2], dp[1][CASE_3] = 1, 1, 0
                    get_count_of_group(2)
                    result = min(result, dp[-1][CASE_3]+2)
                
                if counts[UP][-1] + counts[UP][0] <= W:
                    dp[1][CASE_1], dp[1][CASE_2], dp[1][CASE_3] = 2, (1 if counts[DOWN][0] + counts[DOWN][1] <= W else 2), 1
                    get_count_of_group(2)
                    result = min(result, dp[-1][CASE_2]+1)
                    
                if counts[DOWN][-1] + counts[DOWN][0] <= W:
                    dp[1][CASE_1], dp[1][CASE_2], dp[1][CASE_3] = (1 if counts[UP][0] + counts[UP][1] <= W else 2), 2, 1
                    get_count_of_group(2)
                    result = min(result, dp[-1][CASE_1]+1)
                
            answer.append(result)
        
        print(*answer, sep="\n")
                
    except ValueError or IndexError as e:
        print(e)
