n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

c = []

for i in a:
    c.append(i)

for i in b:
    c.append(b)

c = c.sort() 

for i in c:
    print(i)   

