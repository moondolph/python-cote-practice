#나의 답안
# ans = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# for _ in range(10):
#     a, b = map(int,input().split())
#     ans[a-1:b] = ans[b-1:a-2:-1]    #잘못된 접근. a-2가 -1이 되는 경우가 있기 떄문임. 

# for x in ans:
#     print(x,end=" ")


#나의 답안 2
ans=list(range(1,21))
for _ in range(10):
    a,b = map(int,input().split())
    ans[a-1:b] = ans[a-1:b][::-1]

for x in ans:
    print(x,end=" ")

# #해설답안
# a= list(range(21))        #계산의 편의성을 위하여 인덱스 번호와 값을 일치시킴.
# for _ in range(10):
#     s, e = map(int, input().split())
#     for i in range((e-s+1)//2):           #자리바꾸기
#         a[s+i], a[e-i] = a[e-i], a[s+i]
# a.pop(0)                  #a[0]=0 없애주기 
# for x in a:
#     print(x, end=' ')

