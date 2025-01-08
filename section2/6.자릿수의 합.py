# 나의 답안
def digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10 
    return sum

#참고 : 이런 방법도 있음.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

N = int(input())
a = list(map(int,input().split()))

max_sum = 0
for i in a:
    if max_sum < digit_sum(i):
        max_sum = digit_sum(i)
        num = i
print(num)

#해설 답안
n = int(input())
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum
max =-2147000000

for x in a:
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x
print(res)

