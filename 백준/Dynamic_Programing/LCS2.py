# LCS2
'''https://www.acmicpc.net/problem/9252'''

import sys

if __name__ == "__main__":
    try:
        str1, str2 = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip() 
        
        len1, len2 = len(str1), len(str2)
        
        dp = [["" for _ in range(len2)] for __ in range(len1)]

        for i in range(len1):
            for j in range(len2):
                if str1[i] == str2[j]:
                    pre_str = dp[i-1][j-1] if i > 0 and j > 0 else ""
                    dp[i][j] = pre_str + str1[i]
                else:
                    if i == 0 and j == 0:
                        continue
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) > len(dp[i][j-1]) else dp[i][j-1]
        
        print(len(dp[-1][-1]))
        print(dp[-1][-1])
        
    except ValueError or IndexError as e:
        print(e)
    