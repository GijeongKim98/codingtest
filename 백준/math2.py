def isprime(x): # 시간 복잡도 O((n)^(1/2))
    if x < 2:
        return False
    i = 2

    if x % 2 == 0:
        return False

    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True
'''
# 소수 찾기
try:
    N = int(input())
    str_ = input()
    numbers = list(map(int, str_.split(' ')))
    if N == len(numbers):
        count = 0
        for num in numbers:
            if isprime(num):
                count += 1
        print(count)
    else:
        print('Input Error')
except ValueError and IndexError:
    print('Input Error')

# 소수
try:
    M = int(input())
    N = int(input())
    if 1 <= M <= N <= 10000:
        min_ = -1
        sum_ = 0
        for i in range(M, N+1):
            if isprime(i):
                if min_ == -1:
                    min_ = i
                sum_ += i
        if min_ == -1:
            print(-1)
        else:
            print(sum_)
            print(min_)
    else:
        print('Input Error')
except ValueError and IndexError:
    print('Input Error')

# 소인수 분해
try:
    N = int(input())
    i = 2

    while True:
        if N == 1:
            break

        if N % i == 0:
            print(i)
            N = N // i
        else:
            i += 1

except ValueError:
    print('Input Error')

# 빠른 소수 찾기기
try:
    str_ = input()
    M, N = tuple(map(int, str_.split(' ')))
    if 1 <= M <= N <= 1000000:
        for i in range(M, N+1):
            if isprime(i):
                print(i)
    else:
        print('Input Error')
except ValueError and IndexError:
    print('Input Error')


'''

'''# 베르트랑 공준
try:
    while True:
        n = int(input())
        if n == 0:
            break
        if 1 <= n <= 123456:
            count = 0
            for i in range(n+1, 2*n + 1):
                if isprime(i):
                    count += 1
            print(count)
        else:
            print('Input Error')
except ValueError:
    print('Input Error')

# 에라토스테네스의 체 n까지의 소수 출력

try:
    n = int(input())
    tp_list = [False, False] + [True] * (n-1)
    for i in range(n+1):
        if tp_list[i]:
            for j in range(2*i,n+1,i):
                tp_list[j] = False
    for i in range(n+1):
        if tp_list[i]:
            print(i)

except ValueError:
    print('Error')

# 에라토스테네스의 체를 이용한 베르트랑 공준
try:
    while True:
        n = int(input())
        if n == 0:
            break

        tp_list = [False, False] + [True] * (2*n-1)

        for i in range(2*n+1):
            if tp_list[i]:
                for j in range(2*i,2*n+1,i):
                    tp_list[j] = False

        count = 0
        for i in range(n+1,2*n+1):
            if tp_list[i]:
                count += 1
        print(count)

except ValueError:
    print('Error')

#골든 바흐의 추측
try:
    test_case = int(input())
    for t in range(test_case):
        n = int(input())
        if n % 2 == 0 and 4 <= n <= 10000:
            for i in range(n//2, 1, -1):  # O(n)
                if isprime(i) and isprime(n-i):
                    x, y = i, n-i
                    break
            print(f'{x} {y}')
        else:
            print('Input Error')
except ValueError:
    print('Input Error')
'''

# 에라토스테네스의 체를 이용한 골드바흐의 추측

tp_list = [False, False] + [True] * 9999
for i in range(2,10001):
    if tp_list[i]:
        for j in range(2*i,10001,i):
            tp_list[j] = False

try:
    test_case = int(input())
    for test in range(test_case):
        n = int(input())
        if n % 2 == 0 and 4 <= n <= 10000:
            for i in range(n//2, 1, -1):
                if tp_list[i] and tp_list[n-i]:
                    x, y = i, n - i
                    break
            print(f'{x} {y}')
        else:
            print('Input Error')

except ValueError:
    print('Input Error')
