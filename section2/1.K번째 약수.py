'''
Project ID : Coding test Practice
Program ID : A program that calculates the k-th divisor of a number
Purpose : Practice finding divisors and implementing control flow
Revision History:
    created November 4th in 2024 by Juyong Sim
'''

#----First idea----
N, k = map(int, input().split())
a = list()
for i in range(1, N+1):
    if N % i == 0:
        a.append(i)

try:                            
    print(a[k-1])
except Exception as e:     
    print(e)
    print(-1)

#Try - except is not necessary.


#---Revised idea---
N, K = map(int, input().split())
a = []

# Finding divisors
for i in range(1,N+1):
    if N % i == 0:
        a.append(i)

# Printing K-th divisor
if len(a) >= K:
    print(a[K-1])
else:
    print(-1)

#This takes more time because it calculates all the divisors before printing the result.


#---Answer key explanation---
n, k = map(int, input().split())
cnt=0
for i in range(1,n+1):
    if n%i == 0 :
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

#As shown in the answer key explanation, it is much better to find the answer within the loop.


