'''
# 배수와 약수

try:
    while True:
        n, m = tuple(map(int, input().split(' ')))
        if n == 0 and m == 0:
            break
        if n % m == 0:
            print('multiple')
        elif m % n == 0:
            print('factor')
        else:
            print('neither')
except ValueError or IndexError or ZeroDivisionError:
    print('Input Error')

# 약수
try:
    count = int(input())
    list_ = list(map(int, input().split(' ')))
    if count == 1:
        print(list_[0] ** 2)
    else:
        max_ = list_[0]
        min_ = list_[0]
        for i in range(1,count):
            if list_[i] > max_:
                max_ = list_[i]
            if list_[i] < min_:
                min_ = list_[i]
        print(max_ * min_)

except ValueError or IndexError:
    print("Input Error")

# 최대공약수와 최소공배수

def gcd(n,m):
    r = n % m
    while r != 0:
        n, m = m, r
        r = n % m
    return m

def lcm(n,m):
    return n * m // gcd(n,m)

try:
    n, m = tuple(map(int, input().split(' ')))

    print(gcd(n,m))
    print(lcm(n,m))
except ValueError or IndexError:
    print("Input Error")


# 최소 공배수

def gcd(n,m):
    r = n % m
    while r != 0:
        n, m = m, r
        r = n % m
    return m

def lcm(n,m):
    return n * m // gcd(n,m)

try:
    T = int(input())
    for i in range(T):
        n, m = tuple(map(int, input().split(' ')))
        print(lcm(n,m))
except ValueError or IndexError:
    print("Input Error")

# 검문
# N개 숫자 = t, t % M = r, r이 같은 M을 모두 출력
# 2 <= N <= 100 , 1 <= t <= 1000000000,  t_i != t_j for i != j in N, M > 1

def gcd(n,m):
    r = n % m
    while r != 0:
        n, m = m, r
        r = n % m
    return m

def get_factor(n):
    r1, r2 = [1], [n]
    i = 2
    while i*i <= n:
        if n % i == 0:
            if i != n//i:
                r1.append(i)
                r2.append(n//i)
            else:
                r1.append(i)
        i += 1
    r2.reverse()
    return r1 + r2

# print(get_factor(36))


try:
    N = int(input())
    list_ = []
    min_index = 0
    for i in range(N):
        list_.append(int(input()))
        if list_[min_index] > list_[i]:
            min_index = i

    list_[0], list_[min_index] = list_[min_index], list_[0]

    r = list_[0]
    k = gcd(list_[1] - r, list_[N-1] -r)

    for i in range(1,N):
        gcd_ = gcd(k,list_[i] - r)
        if k != gcd_:
            k = gcd_

    factors = get_factor(k)

    for factor in factors[1:]:
        print(factor, end=' ')

except ValueError or IndexError:
    print('Input Error')

# 링
def gcd(n,m):
    r = n % m
    while r != 0:
        n, m = m, r
        r = n % m
    return m

try:
    N = int(input())
    r = list(map(int, input().split(' ')))
    r_0 = r[0]
    for i in range(1,N):
        k = gcd(r_0,r[i])
        print(f'{r_0 // k}/{r[i] // k}')

except ValueError or IndexError:
    print("Input Error")

# 이항계수
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

try:
    N, K = tuple(map(int, input().split(' ')))
    print(factorial(N) // (factorial(N-K) * factorial(K)))
except ValueError or IndexError:
    print("Input Error")
'''

def gcd(n,m):
    r = n % m
    while r != 0:
        n, m = m, r
        r = n % m
    return m

# 이항 계수 - 2
# n_C_k = n*n-1*...*n-k // k*k-1*k-2*...*1
'''
try:
    N, K = tuple(map(int, input().split(' ')))

    K = (K if K < N-K else N - K)

    list1 = list(range(N-K+1, N+1))

    for num2 in range(K,0,-1):
        while num2 != 1:
            for i in range(0, K):
                if num2 == 1:
                    break

                if list1[i] % num2 == 0:
                    list1[i] = list1[i] // num2
                    num2 == 1

                gcd_ = gcd(list1[i], num2)

                if gcd_ != 1:
                    list1[i] = list1[i] // gcd_
                    num2 = num2 // gcd_

    # list1.sort()
    result = 1

    for num1 in list1:
        result = result * num1
        result = result % 10007

    print(result)

    # print(list1)
except ValueError:
    print('Input Error')
try:
    N, K = tuple(map(int, input().split(' ')))

    K = (K if K < N-K else N - K)

    list1 = list(range(N-K+1, N+1))
    list2 = list(range(K,0,-1))

    for i in range(K-1,-1,-1):
        for j in range(K-1,-1,-1):
            gcd_ = gcd(list1[i],list2[j])
            if gcd_ == 1:
                continue
            list1[i] = list1[i] // gcd_
            list2[j] = list2[j] // gcd_
            if list1[i] == 1:
                break

    result = 1

    for num1 in list1:
        result = result * num1
        result = result % 10007

    print(result)


except ValueError or IndexError:
    print('Input Error')


# 다리 놓기
# 일반항 : a[N][M] = a[N-1][M-1] + a[N][M-1]
# 초깃값 : a[1][j] = j and a[i][i] = 1 and a[i][j] = 0 for i > j

try:
    T = int(input())
    for test in range(T):
        N, M = tuple(map(int, input().split(' ')))
        list_ = [list(range(1,M+1))]
        for i_ in range(N-1):
            list_.append([0] * M)

        for i in range(1,N):
            for j in range(i,M):
                list_[i][j] = list_[i-1][j-1] + list_[i][j-1]

        print(list_[N-1][M-1])

except ValueError or IndexError:
    print("Input Error")

'''

# 패션왕 신해빈
# 옷 가지수(= i) 마다  loop1
# i 를 무엇으로 선택 할 것인가

# tuple 생성기
# 입력 list, tuple 원소 개수
# ex >
# [a,b,c,d], 2  => [(a,b),(a,c),(a,d),(b,c),(b,d),(c,d)]
# [a,b,c,d], 3  => [(a,b,c),(a,)]
# 아래코드 메모리 초과
'''
def get_list(list_, s):
    if s == 1:
        result_ = []
        for dd in list_:
            result_.append([dd])
        return result_

    result = []
    len_ = len(list_)

    for i in range(len_ - s + 1):
        list__ = get_list(list_[i+1:], s-1)
        for j in range(len(list__)):
            list__[j].append(list_[i])
        result += list__
    # print(result)
    return result

# a = get_tuple(['a','b','c','d'],4)
# print(a)

try:
    T = int(input())
    for test in range(T):
        n = int(input())
        dict_ = dict()
        for dress in range(n):
            c = input().split(' ')[1]
            if c in dict_:
                dict_[c] += 1
            else:
                dict_[c] = 1

        sum_ = 0

        kind_list = list(dict_.keys())

        for select in range(1,len(dict_)+1):

            list_list = get_list(kind_list,select)

            for list_ in list_list:
                product = 1

                for k in list_:
                    product *= dict_[k]

                sum_ += product

        print(sum_)
except ValueError:
    print("Input Error")
'''
'''
def get_count(list_,s):
    if s == 1:
        sum_ = 0
        for num in list_:
            sum_ += num
        return sum_

    len_ = len(list_)
    result = 0
    for i in range(len_ - s + 1):
        r = get_count(list_[i+1:], s-1)
        result += r * list_[i]
    return result

sum__ = 0
for i in range(1,5):
    sum__ += get_count([4,3,2,5],i)
print(sum__)


try:
    T = int(input())
    for test in range(T):
        n = int(input())
        dict_ = dict()
        for dress in range(n):
            c = input().split(' ')[1]
            if c in dict_:
                dict_[c] += 1
            else:
                dict_[c] = 1

        sum_ = 0
        kind_list = list(dict_.values())

        list_ = list(map(lambda x: x+1, kind_list))
        #print(list_)
        # print(kind_list)
        result = 1
        for num in list_:
            result *= num
        result -= 1

        print(result)
except ValueError:
    print("Input Error")
'''
# 팩토리얼 0의 개수

# N!에서 뒤에서부터 처음 0이 아닌 숫가 나올 때까지 0의 개수를 구하는 프로그램을 작성

# 10! = 10*9*8*7*6*5*4*3*2*1 = 3628800   0의 개수 2개

# 15! => 3개 15 10 5

# 20 ! => 4개 20 15 10 5

# 25! => 6개 25 20 15 10 5

# 30! => 7개 30 25 15 10 5
# N! => (N // 25) * 2 + (N //5)-(N//25) 의 0의 개수

# 100! = 8 + 20 - 4 = 24
# 120! = 28
# 125! =
'''
try:
    N = int(input())
    p = N // 125
    q = N // 25
    r = N // 5
    print(p+q+r)
except ValueError:
    print("Input Error")
    '''
# 조합 0의 개수

def factorial_0(n):
    sum_ = 0
    p = 5
    while n // p > 0:
        sum_ += n // p
        p *= 5
    return sum_

def factorial_2(n):
    sum_ = 0
    p = 2
    while n // p > 0:
        sum_ += n //p
        p *= 2
    return sum_

# print(factorial_2(125))

try:
    n, m = tuple(map(int, input().split(' ')))
    sum1_0 = factorial_0(n)
    sum2_0 = factorial_0(m)
    sum3_0 = factorial_0(n-m)

    sum1_2 = factorial_2(n)
    sum2_2 = factorial_2(m)
    sum3_2 = factorial_2(n-m)

    p = sum1_0 - sum2_0 - sum3_0
    q = sum1_2 - sum2_2 - sum3_2

    print(min(p,q))

except ValueError or IndexError:
    print("Input Error")