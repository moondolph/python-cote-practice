# #나의 답안
# n, m = map(int,input().split())
# a = list(map(int,input().split()))
# a.sort()
# cnt=0
# lt=0
# rt=n-1
# while True:
#     if a[(rt-lt+1)//2] < m:
#         cnt+=1
#         lt=(rt-lt+1)//2
    
#     elif a[(rt-lt+1)//2] > m:
#         cnt+=1
#         rt=(rt-lt+1)//2
    
#     else:
#         cnt+=1
#         break
# print(cnt)

#ㄴ (rt-lt+1)//2가 아니라 lt+rt//2를 해야 중간 인덱스 값을 구할 수 있다.



#나의 답안2
# n, m = map(int,input().split())
# a = list(map(int,input().split()))
# a.sort()
# cnt=0
# lt=0
# rt=n-1
# while True:
#     if a[(rt+lt)//2] < m:
#         cnt+=1
#         lt=(rt+lt)//2
    
#     elif a[(rt+lt)//2] > m:
#         cnt+=1
#         rt=(rt+lt)//2
    
#     else:
#         cnt+=1
#         break
# print(cnt)

#ㄴ문제를 잘 못 이해하였음. m을 이분검색으로 몇번만에 찾았느냐가 아니라 이분검색으로 m의 인덱스 번호를 구하라는 것임.

#나의 답안3
n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
lt=0
rt=n-1
while True:
    if a[(rt+lt)//2] < m:
        lt=(rt+lt)//2
    
    elif a[(rt+lt)//2] > m:
        rt=(rt+lt)//2
    
    else:
        print((lt+rt)//2 + 1)
        break

#ㄴ 성공 !!



#해설답안
# n, m = map(int,input().split())
# a = list(map(int,input().split()))
# a.sort()
# lt = 0
# rt = n-1
# while lt<=rt:
#     mid=(lt+rt)
#     if a[mid]==m:
#         print(mid+1)
#         break
#     elif a[mid]>m:
#         rt=mid-1
#     else:
#         lt=mid+1


