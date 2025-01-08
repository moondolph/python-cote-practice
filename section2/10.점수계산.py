#나의 답안
n = int(input())
a = list(map(int,input().split()))
point = 0
extra = 0
for i in range(n):
    if a[i]==0:
        extra=0
    else:
        extra+=1
        point+=extra
print(point)