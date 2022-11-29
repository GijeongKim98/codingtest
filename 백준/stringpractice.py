'''
# ASCII CODE

try:
    char = input()
    print(ord(char))
except ValueError:
    print('입력 오류')

# 숫자의 합

try:
    N = int(input())
    str_ = input()
    if N == len(str_):
        sum_ = 0

        for num in str_:
            number = int(num)
            sum_ += number
    print(sum_)
except ValueError or NameError:
    print('Input Error')

try:
    str_ = input()

    if str_.isalpha() and str_.islower():
        list_ = [-1] * (ord('z') - ord('a') + 1)  # length = 26

        for i, char in enumerate(str_):
            if list_[ord(char) - ord('a')] == -1:
                list_[ord(char) - ord('a')] = i

        for index in list_:
            print(index, end=' ')

    else:
        print('Input Error')
except ValueError:
    print('Input Error')


# 문자열 반복

try:
    T = int(input())
    for i in range(T):
        r_str = input()
        r_str = r_str.split(' ')
        R = int(r_str[0])
        str_ = r_str[1]
        for char in str_:
            print(char*R, end='')
        print()
except ValueError:
    print('InputError')


# 단어 공부

dict_ = dict()

try:
    str_ = input()
    if len(str_) < 10000000 and str_.isalpha():
        str_u = str_.upper()

        for char in str_u:
            if char not in dict_:
                dict_[char] = 1
            else:
                dict_[char] += 1

        max_ = '_'
        pre_max = '__'

        dict_[max_] = 0
        dict_[pre_max] = 0

        # print(dict_)

        for char_ in dict_.keys():
            if dict_[max_] <= dict_[char_]:
                pre_max = max_
                max_ = char_

        if dict_[pre_max] == dict_[max_]:
            print('?')
        else:
            print(max_)
    else:
        print('Input Error')

except ValueError:
    print('Error')


# 단어의 개수

str_ = input()
if len(str_) < 10000000:
    str_ = str_.strip()
# print(str_.split(' '))
    if str_ == '':
        print(0)
    else:
        print(len(str_.split(' ')))


# 상수

try:
    str_ = input()
    if '0' not in str_:
        numbers = str_.split(' ')
        s_num1 = int(numbers[0][::-1])
        s_num2 = int(numbers[1][::-1])

        if s_num1 < s_num2:
            print(s_num2)
        else:
            print(s_num1)
except ValueError or IndexError:
    print('Input Error')


# 다이얼

# str_ -> [문자 -> 숫자] -> 숫자 -> 시간

def char_num(c):
    if c.isalpha() and c.isupper():
        rst = ord(c) - ord('A')
        if rst // 15 == 0:
            return rst // 3 + 2
        elif rst // 19 == 0:
            return 7
        elif rst // 22 == 0:
            return 8
        else:
            return 9
    else:
        return -1

# print(char_num('J'))

try:
    str_ = input()
    # print(len(str_))
    if 2 <= len(str_) <= 15:
        numbers = []
        for char in str_:
            numbers.append(char_num(char))
        # print(numbers)
        sum_t = 0
        for num in numbers:
            if num == -1:
                print('Input error')
            else:
                sum_t += num + 1

        print(sum_t)
    else:
        print('Input Error')

except ValueError or IndexError:
    print('Input Error')

# 크로아티아 알파벳 : c= // c- // dz= // d- // lj // nj // s= // z=

try:
    str_ = input()
    if len(str_) <= 100:
        sum_alpha = 0
        for i, char in enumerate(str_):
            sum_alpha += 1
            if char == '=' or char == '-':
                if str_[i-1] == 'z' and str_[i-2] == 'd':
                    sum_alpha -= 2
                else:
                    sum_alpha -= 1
            elif char == 'j' and (str_[i-1] == 'l' or str_[i-1] == 'n'):
                sum_alpha -= 1
        print(sum_alpha)
    else:
        print('Input Error')
except IndexError:
    print('Input Error')

'''

# 그룹 단어 체커
def is_group_word(str_):
    pre_char = ''
    set_ = set()

    for char in str_:
        if char not in set_:
            set_.add(char)
            pre_char = char
        elif pre_char != char:
            return False
    return True

try:
    N = int(input())
    sum_group = 0

    for i in range(N):
        str_ = input()

        if str_.isalpha() and str_.islower():
            sum_group += (1 if is_group_word(str_) else 0)

        else:
            print('Input Error')

    print(sum_group)

except ValueError:
    print('Input Error')


