#나의 답안 1
#소수가 아닌 애들을 빼는 접근법
# #  답이 나오긴 하는데 시간 초과로 안됌 --> 모든 숫자를 다 뒤지니까 안됨
# n = int(input())
# discount = 0
# for i in range(2,n+1):
#     for j in range(2,i):
#         if (i % j == 0) :
#             discount += 1
#             break
# print(n-1-discount)

#나의 답안 2
# n = int(input())
# a = []
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         a.append[i]         #i가 7일때 j가 2,3,4,5,6이면 7이 리스트에 5번 다 들어가잖아.
# print(len(a))

#해설답안 
n=int(input())
a=[0] * (n+1)
cnt=0
for i in range(2, n+1):
    if a[i] == 0:
        cnt+=1
        for j in range(i,n+1,i):
            a[j]=1
print(cnt)

