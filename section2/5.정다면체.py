#첫번째 답안
n, m = map(int,input().split())
a=list()

for i in range(1,n+1):
    for j in range(1,j+1):
        a[i+j]+=1

n = a.count(a.max)  #가장 확률 높은 수의 개수
ans = a.index(a.max) #가장 확률 높은 수의 인덱스, 인덱스=가장 확률 높은 수

for i in n:
    print(ans + i, end=" ")

#두번째 답안 
n, m = map(int,input().split())
a = [0] * (n + m + 1)   #list의 요소의 값들을 초기화. +1을 하는 이유는 인덱스 번호는 0부터 시작하니까.

for i in range(1,n+1):
    for j in range(1,m+1):
        a[i+j]+=1

n = a.count(max(a))  #가장 확률 높은 수의 개수
ans = a.index(max(a)) #가장 확률 높은 수의 인덱스, 인덱스=가장 확률 높은 수

for i in range(n):
    print(ans + i, end=" ")  #이 풀이 방식은 가장 확률 높은 수들은 모여 있다는 원리를 적용하였음 




#해설답안
n,m = map(int,input().split())
cnt = [0] * (n+m+1)
max=-2147000000

for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j]+=1

for i in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]

for i in range(n+m+1):
    if cnt[i]==max:
        print(i, end=" ")
