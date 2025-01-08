'''
Project ID : Coding test Practice
Program ID : A program that outputs the student's order number who is the most closest to the average 
Purpose : Output the average number and its index number from a specified range of numbers 
Revision History:
    created November 5th in 2024 by Juyong Sim
'''

#//First idea
N = int(input())
a = list(map(int,input().split()))
sum=0
for i in a:
    sum += i
avg = round(sum / N) #rounding to the first decimal place

diff=99999999
ans = 0
num = 0

for i in range(N):
    if diff > abs(avg - a[i]) :
        diff = abs(avg- a[i])
        ans = i+1
        num = a[i]

    elif diff == abs(avg - a[i]):
        if a[i] > num :
            ans = i+1
print(avg, ans)


#//Revised idea
N = int(input())
a = list(map(int,input().split()))
# avg = round(sum(a) / N)   round함수는 round_half_even 방식이어서 이렇게 하면 안됨.
#avg = int(format(sum(arr) / len(arr), ".0f")) format함수도 round_half_even 방식임.
avg = int((sum(a) / N)+0.5)     #이렇게 하면 round_half_up방식으로 수정 가능

diff = float('inf') #initialize to infinity

for i in range(N):
    if diff > abs(avg - a[i]):
        diff = abs(avg - a[i])
        ans = i+1
        num = a[i]
    
    elif diff == abs(avg - a[i]):
        if a[i] > num:
            ans = i+1

print(avg, ans)





#해설답안
n = int(input())
a = list(map(int,input().split()))
# ave = round(sum(a)/n)         round 함수는 round_half_even 방식이어서 안됨.
ave = int((sum(a)/n)+0.5)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)