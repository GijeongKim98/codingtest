# 출근 기록
'''https://www.acmicpc.net/problem/14238'''

# Method 1 : BackTracking => 시간초과
'''
import sys
import time

A, B, C = 0, 1, 2

def dfs(count_a, count_b, count_c, p, pp):
    
    if count_a == 0 and count_b == 0 and count_c == 0:
        return True
    
    if (count_a, count_b, count_c) in dp:
        return False
    
    if count_c and p != C and pp != C:
        if dfs(count_a, count_b, count_c-1, C, p):
            answer.append("C")
            return True
    if count_b and p != B:
        if dfs(count_a, count_b-1, count_c, B, p):
            answer.append("B")
            return True
    if count_a:
        if dfs(count_a-1, count_b, count_c, A, p):
            answer.append("A")
            return True
    else:
        dp.add((count_a, count_b, count_c))
        return False
        

if __name__ == "__main__":
    try:
        # start_time = time.time()
        string = sys.stdin.readline().rstrip()
        
        count = {c : 0 for c in range(3)}
        
        for c in string:
            count[ord(c) - ord("A")] += 1
    
        answer = []
        dp = set()
        
        if dfs(count[A], count[B], count[C], A, A):
            answer = reversed(answer)
            print("".join(answer))
            
        else:
            print(-1)
            
        # print(time.time() - start_time)
        
    except ValueError or IndexError as e:
        print(e)'''
        
# answer_code
# Reference :https://hjp845.tistory.com/166

# Method 2: DP
# 5차원 배열을 만들어 이미 조사한 경우라면 더 이상 조사를 하지 않는다.

import sys
import time

A, B, C = 0, 1, 2

def dfs(c_a, c_b, c_c, p, pp):
    if c_a == 0 and c_b == 0 and c_c == 0:
        return True
    
    if dp[c_a][c_b][c_c][p][pp]:
        return False
    
    dp[c_a][c_b][c_c][p][pp] = 1
    
    idx = c_a+c_b+c_c
    
    if c_a:
        answer[idx] = "A"
        if dfs(c_a-1, c_b, c_c, A, p):
            return True
    
    if c_b and p != B:
        answer[idx] = "B"
        if dfs(c_a, c_b-1, c_c, B, p):
            return True
    
    if c_c and p != C and pp != C:
        answer[idx] = "C"
        if dfs(c_a, c_b, c_c-1, C, p):
            return True
    
    return False

if __name__ == "__main__":
    try:
        s_t = time.time()
        string = sys.stdin.readline().rstrip()
        len_ = len(string)
        dp = [[[[[0 for _ in range(3)] for _ in range(3)] for _ in range(len_+1)] for _ in range(len_+1)] for _ in range(len_+1)]

        count = [0, 0, 0]
        
        for c in string:
            count[ord(c) - ord("A")] += 1
        
        answer = [0 for _ in range(len_+1)]
        
        count += [0, 0]
        
        if dfs(*count):
            print("".join(answer[1:]))
        else:
            print(-1)
        
        e_t = time.time()
        
        print(f"{e_t-s_t:.5f} sec")
        
    except ValueError or IndexError as e:
        print(e)
     

