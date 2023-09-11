# helloworld 출력
print('Hello World!')

# We love krill
print('강한친구 대한육군\n강한친구 대한육군')
'''
# 두수의 합
a = input()

numbers = a.split(' ')

if len(numbers) > 2:
    print('입력값 오류')

try:
    a = int(numbers[0])
    b = int(numbers[1])

    if 0 < a < 10 and 0 < b < 10:
        print(a+b)

except ValueError:
    print('입력된 값은 오류가 있습니다.')
'''
# 두수의 차
'''https://www.acmicpc.net/problem/1001'''
'''
try:
    a, b = tuple(map(int, input().split(' ')))
    if 0 < a < 10 and 0 < b < 10:
        print(a-b)

except ValueError:
    print('입력된 값은 오류가 있습니다.')
'''

# 두수의 곱
'''https://www.acmicpc.net/problem/10998'''
'''try:
    a, b = tuple(map(int, input().split(' ')))
    if 0 < a < 10 and 0 < b < 10:
        print(a*b)

except ValueError:
    print('입력된 값은 오류가 있습니다.')


# 두수의 나눗셈
'''
'''https://www.acmicpc.net/problem/1008'''
'''
try:
    a, b = tuple(map(int, input().split(' ')))
    if 0 < a < 10 and 0 < b < 10:
        print(a/b)

except ValueError:
    print('입력된 값은 오류가 있습니다.')
'''
# 두수의 사칙연산
'''https://www.acmicpc.net/problem/10869'''
'''
try:
    a, b = tuple(map(int, input().split(' ')))
    if 0 < a < 10000 and 0 < b < 10000:
        print(a + b)
        print(a - b)
        print(a * b)
        print(a // b)
        print(a % b)


except ValueError:
    print('입력된 값은 오류가 있습니다.')

# ??!
str_ = input()

if 0 < len(str_) < 51 and str_.isalpha() and str_.islower():
    print(str_ + '??!')
else:
    print('입력값 오류')
'''
# 1998년생인 내가 태국에서는 2541년생?!
'''
delta = 2541 - 1998

y = input()

try:
    y = int(y)

    if 1000 <= y <= 3000:
        print(y - delta)
    else:
        print('입력값 오류')

except ValueError:
    print('입력값 오류')

# 킹,퀸,룩,비숍,나이트,폰

numbers = [1,1,2,2,2,8]

str_ = input()

numbers_str = str_.split(' ')

if len(numbers) == 6:
    try:
        for i, number in enumerate(numbers_str):
            print(numbers[i] - int(number), end=' ')

    except ValueError:
        print('입력 오류')
else:
    print('입력 오류')
'''
# 나머지
'''
str_ = input()

numbers = str_.split(' ')

list_ = []

try:
    for number in numbers:
       a = int(number)
       list_.append(a)

    print((list_[0] + list_[1]) % list_[2])
    print(((list_[0] % list_[2]) + (list_[1] % list_[2])) % list_[2])

    print((list_[0] * list_[1]) % list_[2])
    print(((list_[0] % list_[2]) * (list_[1] % list_[2])) % list_[2])

except ValueError:
    print('입력 오류')
'''
'''
# 곱셈

str1 = input()
str2 = input()

if len(str1) == 3 and len(str2) == 3:
    try:
        a = int(str1)
        b = []

        for number in str2:
            b.append(int(number))

        b[0], b[2] = b[2], b[0]

        sum = 0

        for i, num in enumerate(b):
            product = a * num
            print(product)
            sum += product * (10 ** i)

        print(sum)

    except ValueError:
        print('입력 오류')

else:
    print('입력 오류')

'''
# # 고양이 출력
# str1 = '\\    /\\'
# str2 = ' )  ( \')'
# str3 = '(  /  )'
# str4 = ' \\(__)|'

# print(str1)
# print(str2)
# print(str3)
# print(str4)

# # 강아지 출력
# # |\_/|
# # |q p|   /}
# # ( 0 )"""\
# # |"^"`    |
# # ||_/=\\__|

# print('|\\_/|')
# print('|q p|   /}')
# print('( 0 )\"\"\"\\')
# print('|\"^\"`    |')
# print('||_/=\\\\__|')

# print('\n\n\n\n\n\n')

# # 새싹 출력
# #          ,r'"7
# # r`-_   ,'  ,/
# #  \. ". L_r'
# #    `~\/
# #       |
# #       |
# print('         ,r\'\"7')
# print('r`-_   ,\'  ,/')
# print(' \\. \". L_r\'')
# print('   `~\\/')
# print('      |')
# print('      |')


# # 음계
# '''https://www.acmicpc.net/problem/2920'''

# import sys
# try:
#     numbers = list(map(int, sys.stdin.readline().split(' ')))

#     def is_ascending():
#         for i in range(8):
#             if i + 1 != numbers[i]:
#                 return False
#         return True
#     def is_descending():
#         for j in range(8):
#             if 8 - j != numbers[j]:
#                 return False
#         return True

#     if is_ascending():
#         print('ascending')
#     elif is_descending():
#         print('descending')
#     else:
#         print('mixed')
# except ValueError or IndexError:
#     print('Input Error')

# # 검증수
# '''https://www.acmicpc.net/problem/2475'''

# import sys
# try:
#     numbers = list(map(int, sys.stdin.readline().split(' ')))
#     sq_num = list(map(lambda x : (x**2 % 10), numbers))
#     rlt = 0
#     for sq in sq_num:
#         rlt = (rlt+sq) % 10

#     print(rlt)
# except ValueError or IndexError:
#     print('Input Error')

# # N 찍기
# '''https://www.acmicpc.net/problem/2741'''

# import sys
# try:
#     n = int(sys.stdin.readline())
#     for i in range(1,n+1):
#         print(i)
# except ValueError:
#     print('Input Error')

# # 기찍 N
# '''https://www.acmicpc.net/problem/2742'''

# import sys
# try:
#     n = int(sys.stdin.readline())
#     for i in range(n,0,-1):
#         print(i)
# except ValueError:
#     print('Input Error')

# # 펜린드롭수
# '''https://www.acmicpc.net/problem/1259'''

# import sys
# try:
#     while True:
#         numbers = sys.stdin.readline()
#         if numbers == '0':
#             break
#         len_ = len(numbers) - 1
#         c = 0
#         for i in range(len(numbers)//2):
#             if numbers[i] != numbers[len_-i]:
#                 c = 1
#                 break
#         if c == 1:
#             print('no')
#         else:
#             print('yes')
# except ValueError or IndexError:
#     print('error')

import time

s = time.time()
a = []
for i in range(100000):
    a.append(i)

# for i in range(100000):
#     k = i
#     q = k
    

for i in a:
    q = i

print(time.time() - s) 
