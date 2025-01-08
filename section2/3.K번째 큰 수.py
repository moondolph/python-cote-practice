'''
Project ID : Coding test Practice
Program ID : Output the k-th largest sum from all possible combinations of three cards drawn from N cards, where each card has a natural number between 1 and 100.
Purpose : Calculate the k-th largest sum from all combinations of three cards and ensure that the k-th value exists.
Revision History:
    created November 5th in 2024 by Juyong Sim
'''
#///First idea
N, K = map(int, input().split())
a = list(map(int,input().split()))

set = {}
for i in range(0,N-2):
    for j in range(1, N-1):
        for k in range(2, N):
            sum = a[i] + a[j] + a[k]
            set.add(sum)
ans = list(set)
ans.sort(reverse=True)
print(ans[K-1])


#///revised idea
N, K = map(int, input().split())
a = list(map(int,input().split()))
 
ans = set()    
# ans= {} empty dictionary / ans = set() empty set

#range should be fixed
for i in range(N-2):            
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = a[i] + a[j] + a[k]
            ans.add(sum)        #"Set" is unordered data structure.
ans = list(ans)                 #It should be changed to list to use indexing and sort method.
ans.sort(reverse=True)
print(ans[K-1])



#///Answer
n, k = map(int, input().split())
a = list(map(int,input().split()))
# a.sort(reverse=True)
# 내림차순으로 정렬 미리 할 필요가 없다
# set을 쓴다면 ->어차피 set은 무작위가 담겨서 나중에 list로 바꾸고 다시 정렬해야함.

res=set()   #더한 값이 담기는 set 자료구조로 중복을 제거해줌. 단점은 무작위로 담김..

for i in range(n-2):
    for j in range(i+1,n-1):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m]) #이렇게 담으면 unordered로 담긴다.

res=list(res)       #리스트로 바꿔줘야 인덱싱과 sort가 가능
res.sort(reverse=True)
print(res[k-1])