##나의 답안
def reverse(x):
    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10    
    return reversed_num
#숫자 뒤집기 다른 방식 
#print(str(n)[::-1])   이 방식은 n=1000이면 0001이렇게 나옴

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x):   #x까지 돌릴 필요가 없다. int(x**2) + 1   숫자의 제곱근까지만 나누어 보면 소수 여부를 확인할 수 있기 때문이다.
        if x % i == 0:
            break          #break가 아니라 return False를 하는 것이 더 좋다.
    else:
        return True

n = int(input())
a = list(map(int,input().split()))
for i in a:
    reversed_num = reverse(i)
    if isPrime(reversed_num):
        print(reversed_num, end=' ')

#해설답안
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):
    if x==1 :
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True
    
n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')



#소수를 판별할 때, 어떤 수 x의 약수는 그 수의 제곱근 이하에 반드시 하나씩 존재합니다. 예를 들어, 36의 약수는 1, 2, 3, 4, 6, 9, 12, 18, 36인데, 제곱근인 6 이하에 모든 약수가 존재합니다.
#따라서, x의 제곱근까지만 검사하면, 그 이후로는 추가적인 검사가 필요하지 않습니다. 이는 소수 판별에서 매우 중요한 최적화 포인트입니다.