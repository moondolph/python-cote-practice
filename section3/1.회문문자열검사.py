#나의 답안
# n = int(input())
# for i in range(1,n+1):
#     a = input().upper()
#     if a == a[::-1]:
#         print(f"#{i} YES")
#     else:
#         print(f"#{i} NO")


#해설답안
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j]!=s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

