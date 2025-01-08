#나의 답안
a = input()
number=""
for i in range(len(a)):     # for i in a: 이렇게 바로 문자열에 접근 가능
    if a[i].isdigit():      # isdigit은 모든 2의 10제곱도 검사. isdecimal은 0~9까지만
        number+=a[i]
number = int(number)        # number = number * 10 + int(i)의 방식도 있음.
cnt=0
for i in range(1,number+1):
    if number % i == 0:
        cnt+=1
print(number)
print(cnt)


#해설 답안
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)

cnt = 0
for i in range(1, res+1):
    if res % i == 0 :
        cnt += 1
print(cnt)

