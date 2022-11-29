'''
# 알고리즘 수업 - 피보나치 수 1

try:
    n = int(input())
    count1, count2 = 0, 0
    def fib(x):
        global count1
        if x == 1 or x == 2:
            count1 += 1
            return 1
        else:
            return fib(x-1) + fib(x-2)

    f = [0] * (n+1)
    def fibonacci(x):
        global count2

        f[1], f[2] = 1, 1
        for i in range(3,x+1):
            count2 += 1
            f[i] = f[i-1] + f[i-2]

        return f[x]

    fib(n)
    fibonacci(n)

    print(f'{count1} {count2}')

except ValueError:
    print("Input Error")

# 신나는 함수 실행
try:
    list_ = [[[1] * 21 for _ in range(21)] for __ in range(21)]

    for i in range(1,21):
        for j in range(1,21):
            for k in range(1,21):
                if i < j < k:
                    list_[i][j][k] = list_[i][j][k-1] + list_[i][j-1][k-1] - list_[i][j-1][k]
                else:
                    list_[i][j][k] = list_[i-1][j][k] + list_[i-1][j-1][k] + list_[i-1][j][k-1] - list_[i-1][j-1][k-1]

    while True:
        a,b,c = tuple(map(int, input().split(' ')))

        if a == -1 and b == -1 and c == -1:
            break

        if a > 20 or b > 20 or c > 20:
            print(f'w({a}, {b}, {c}) = {list_[20][20][20]}')

        elif a < 1 or b < 1 or c < 1:
            print(f'w({a}, {b}, {c}) = {1}')

        else:
            print(f'w({a}, {b}, {c}) = {list_[a][b][c]}')

except ValueError or IndexError:
    print("Input Error")


# 신나는 함수 실행
# 재귀함수를 사용하자

try:
    graph = [[[0] * 21 for _ in range(21)] for __ in range(21)]

    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        if a > 20 or b > 20 or c > 20:
            return w(20,20,20)

        if graph[a][b][c] != 0:
            return graph[a][b][c]

        if a < b < c:
            graph[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
            return graph[a][b][c]

        graph[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return graph[a][b][c]

    while True:
        a, b, c = tuple(map(int, input().split(' ')))
        if a == -1 and b == -1 and c == -1:
            break
        else:
            print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

except ValueError or IndexError:
    print("Input Error")
'''

# 01 타일
''' https://www.acmicpc.net/problem/1904 '''
'''
try:
    N = int(input())
    count_list = [1] * (N+1)

    for i in range(2,N+1):
        count_list[i] = (count_list[i-1] + count_list[i-2]) % 15746

    print(count_list[N])

except ValueError:
    print('Input Error')
'''
# 파도반 수열
'''https://www.acmicpc.net/problem/9461'''
'''
try:
    testcase = int(input())

    length_list = [0, 1, 1, 1, 2] + [0] * 96

    for test in range(testcase):
        N = int(input())
        for i in range(5,N+1):
            length_list[i] = length_list[i-1] + length_list[i-5]
        print(length_list[N])

except ValueError:
    print("Input Error")
    
'''
'''
# 연속합

try:
    n = int(input())
    numbers = list(map(int, input().split(' ')))

    max_ = numbers[0]
    sum_ = numbers[0]

    for i in range(1, n):
        if sum_ < 0:
            sum_ = 0
        sum_ += numbers[i]
        if max_ < sum_:
            max_ = sum_

    print(max_)

except ValueError or IndexError:
    print('Input Error')
'''

# RGB 거리
'''https://www.acmicpc.net/problem/1149'''
'''
try:
    N = int(input())

    pre_r, pre_g, pre_b = tuple(map(int,input().split(' ')))

    for i in range(1, N):
        r,g,b = tuple(map(int,input().split(' ')))

        r += (pre_g if pre_g < pre_b else pre_b)
        g += (pre_r if pre_r < pre_b else pre_b)
        b += (pre_r if pre_r < pre_g else pre_g)

        pre_r, pre_g, pre_b = r, g ,b

    min_ = pre_r

    if min_ > pre_g:
        min_ = pre_g
    if min_ > pre_b:
        min_ = pre_b

    print(min_)

except ValueError or IndexError:
    print('Input Error')

'''

# 정수 삼각형
'''https://www.acmicpc.net/problem/1932'''
'''
try:
    n = int(input())
    pre_ = [int(input())]
    list_ = pre_[:]
    for i in range(1, n):
        list_ = list(map(int,input().split(' ')))

        list_[0] += pre_[0]
        for j in range(1, i):
            list_[j] += (pre_[j] if pre_[j] > pre_[j-1] else pre_[j-1])
        list_[i] += pre_[i-1]

        if i != n-1:
            pre_ = list_[:]

    print(max(list_))
except ValueError or IndexError:
    print('Input Error')
'''

# 계단 오르기
'''https://www.acmicpc.net/problem/2579'''
'''
try:
    step = int(input())
    score1 = [0] * (step + 1)
    score2 = [0] * (step + 1)

    t1 = int(input())
    score1[1] = t1
    score2[1] = t1

    for i in range(2,step+1):
        t = int(input())
        score1[i] = t + score2[i-1]
        score2[i] = t + (score1[i-2] if score1[i-2] > score2[i-2] else score2[i-2])

    print((score1[step] if score1[step] > score2[step] else score2[step]))

except ValueError or IndexError:
    print('Input Error')
'''

# 1로 만들기
'''https://www.acmicpc.net/problem/1463'''
'''
try:
    N = int(input())
    list_ = [0,0] + list(range(N))

    for i in range(2,N+1):
        if i % 6 == 0:
            list_[i] = min(list_[i//3], list_[i//2], list_[i-1]) + 1
        elif i % 3 == 0:
            list_[i] = min(list_[i//3], list_[i-1]) + 1
        elif i % 2 == 0:
            list_[i] = min(list_[i//2], list_[i-1]) + 1
        else:
            list_[i] = list_[i-1] + 1

    print(list_[N])

except ValueError:
    print("Input Error")
'''
# 쉬운 계단의 수
'''https://www.acmicpc.net/problem/10844'''
# 길이가 n인 계단의 수의 개수를 알아보자
# n = 1 : [1,2,3,4,5,6,7,8,9] => [0,1,1,1,1,1,1,1,1,1] => 9
# n = 2 : [10,12,21, ... ,87,89,98] => [1,1,2,2,2,2,2,2,2,1] => 17
# n = 3 : [101,...,989] => [1,3,3,4,4,4,4,4,3,2] => sum
'''
try:
    N = int(input())
    list_ = [0] + [1] * 9
    next_ = [0] * 10

    for i in range(1,N):
        next_[0] = list_[1]
        for j in range(1,9):
            next_[j] = list_[j-1] + list_[j+1]
        next_[9] = list_[8]

        # print(next_)
        list_ = next_[:]

    rlt = 0
    for c in list_:
        rlt += c

    print(rlt % 1000000000)
except ValueError:
    print("Input Error")
'''

'''
# 포도주 시식
# 연속 3잔 불가능 최대 2잔 => 백준 계단 오르기 문제와 유사
# 최대로 많이 먹었을 때 얼마나 먹을 수 있을까?

# cup : 6  10  13  9   8   19
# max : 6  16  23  28  33  50

# case 1 : 한칸 전의 포도주를 마신 경우 dp_arr[i-3] + number[i-1] + number[i]
# case 2 : 두칸 전의 포도주를 마신 경우 rlt(가장 큰 값) + number[i]
# if dp_arr[i-1] > dp_arr[i] => dp_arr[i] = dp_arr[i-1]

try:
    n = int(input())
    w = [int(input()) for _ in range(n)]
    dp_arr = [0] * n

    for i in range(n):
        if i == 0:
            dp_arr[i] = w[i]
        elif i == 1:
            dp_arr[i] = w[i] + w[i-1]
        else:
            dp_arr[i] = max(dp_arr[i-2]+ w[i], dp_arr[i-3] + w[i-1] + w[i])

        if dp_arr[i-1] > dp_arr[i]:
            dp_arr[i] = dp_arr[i-1]
    print(dp_arr[n-1])
except ValueError or IndexError:
    print('Input Error')
'''


# 가장 긴 증가하는 부분 수열
'''https://www.acmicpc.net/problem/11053'''
'''
try:
    N = int(input())
    numbers = list(map(int, input().split(' ')))
    dp_arr = [1] * N
    rlt = 0
    for i, number in enumerate(numbers):
        max_ = 0
        for j in range(i):
            if number > numbers[j]:
                max_ = (max_ if max_ > dp_arr[j] else dp_arr[j])
        dp_arr[i] = max_ + 1

        if dp_arr[i] > rlt:
            rlt = dp_arr[i]
    
    print(rlt)
except ValueError or IndexError:
    print("Input Error")
'''

# 가장 긴 바이토닉 부분 수열
'''https://www.acmicpc.net/problem/11054'''
'''
try:
    N = int(input())
    numbers = list(map(int,input().split(' ')))
    dp_arr1 = [1] * N
    dp_arr2 = [1] * N

    for i in range(N):
        j = N-1-i
        max1 = 0
        max2 = 0

        for p in range(i):
            if numbers[i] > numbers[p]:
                max1 = (max1 if max1 > dp_arr1[p] else dp_arr1[p])

        for q in range(j,N):
            if numbers[j] > numbers[q]:
                max2 = (max2 if max2 > dp_arr2[q] else dp_arr2[q])


        dp_arr1[i] = max1 + 1
        dp_arr2[j] = max2 + 1

    rlt = 0

    for idx in range(N):
        sum_ = dp_arr1[idx] + dp_arr2[idx]
        rlt = (rlt if rlt > sum_ else sum_)

    print(rlt-1)


except ValueError or IndexError:
    print('Input Error')
'''
# 전깃줄
'''https://www.acmicpc.net/problem/2565'''
'''
try:
    n = int(input())
    dict_ = dict()

    for i in range(n):
        tup_ = tuple(map(int, input().split(' ')))
        dict_[tup_[0]] = tup_[1]

    list_ = sorted(dict_.keys())
    numbers = [dict_[i] for i in list_]

    dp_arr = [1] * n
    rlt = 0
    for i, number in enumerate(numbers):
        max_ = 0
        for j in range(i):
            if number > numbers[j]:
                max_ = (max_ if max_ > dp_arr[j] else dp_arr[j])
        dp_arr[i] = max_ + 1

        if dp_arr[i] > rlt:
            rlt = dp_arr[i]

    print(n - rlt)

except ValueError:
    print("Input Error")
'''

# LCS
'''https://www.acmicpc.net/problem/9251'''
'''
try:
    str1 = input()
    str2 = input()
    len1 = len(str1)
    len2 = len(str2)
    dp_arr = [[0] * (len1+1) for _ in range(len2+1)]

    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if str1[j-1] == str2[i-1]:
                dp_arr[i][j] = dp_arr[i-1][j-1] + 1
            else:
                dp_arr[i][j] = max(dp_arr[i][j-1],dp_arr[i-1][j])

    print(dp_arr[len2][len1])

except ValueError:
    print("Input Error")
'''

# 평범한 배낭
# 주어진 무게를 초과 x,  최대 가치를 원함
'''https://www.acmicpc.net/problem/12865'''

try:
    N, K = tuple(map(int, input().split(' ')))
    w, v = [], []
    for i in range(N):
        w_, v_ = tuple(map(int, input().split(' ')))
        w.append(w_)
        v.append(v_)

    dp_arr = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(1,K+1):
            if w[i-1] > j:
                dp_arr[i][j] = dp_arr[i-1][j]
            else:
                dp_arr[i][j] = max(dp_arr[i-1][j], dp_arr[i-1][j-w[i-1]] + v[i-1])

    print(dp_arr[N][K])

except ValueError or IndexError:
    print("Input Error")





