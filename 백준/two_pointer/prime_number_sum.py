# 소수의 연속합
'''https://www.acmicpc.net/problem/1644'''


CONS = 4_000_000

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

if __name__ == "__main__":
    
    N = int(input())
    
    prime_numbers = prime_list(N)
    K = len(prime_numbers)
    
    answer = 0
    
    # Method 1 : 모든 합을 구하고 N과 일치하는 것을 찾아냄
    # for i in range(K):
    #     for j in range(i+1,K+1):
    #         sum_ = sum(prime_numbers[i:j])
    #         if sum_ > N:
    #             break
    #         elif sum_ == N:
    #             # print(prime_numbers[i:j])
    #             answer += 1
    
    # Method 2
    # refer : https://www.acmicpc.net/source/54252298
    sum_ = 0
    
    e = iter(prime_numbers)
    
    for s in prime_numbers:
        sum_ += s
        while sum_ > N:
            sum_ -= next(e)
        
        if sum_ == N:
            answer += 1
    
    
        
    
    
    print(answer)