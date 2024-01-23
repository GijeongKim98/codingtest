# list a의 합을 구하는 함수
def solve(a):
    sum_ = 0
    for number in a:
        sum_ += number
    return sum_


# self number

def getlist(n):
    if n < 0:
        return []

    list_ = []
    while n != 0:
        r = n % 10
        n = n // 10
        list_.append(r)
    list_.reverse()
    return list_


def d(n):  # n은 정수 입력

    list_ = getlist(n)

    result = n

    for i in list_:
        result += i

    return result


def get_self_number(n):
    set_ = set()
    result = []

    for i in range(1, n + 1):
        if i not in set_:
            result.append(i)
        set_.add(d(i))

    return result

# result = getSelfNumber(10000)

# for number in result:
#     print(number)


##############################

# 한수 : 1~99까지는 다 한수임

def is_ap(a):
    len_a = len(a)
    if len_a < 3:
        return True
    d = (a[0] - a[-1]) / (len_a - 1)
    for i in range(len_a - 1):
        if d != a[i] - a[i+1]:
            return False
    return True

# print(is_ap([1,2,3]))

# n보다 작은 한수 출력
def han_number(n):
    count = 99

    if n < 100:
        return n

    for i in range(100, n+1):
        list_ = getlist(i)
        if is_ap(list_):
            count += 1

    return count

try:
    N = int(input())
    print(han_number(N))
except ValueError:
    print('Input error')
