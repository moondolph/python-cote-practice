#나의 답안
n = int(input())
max_prize=0
for _ in range(n):
    a = list(map(int,input().split()))
    unique_a = set(a)
    if len(unique_a) == 1:
        prize = 10000 + (a[0] * 1000)
    elif len(unique_a) == 2:
        prize = 1000 + ([x for x in unique_a if a.count(x)==2][0] * 100)
    else:
        prize = (max(a)*100)
    if prize > max_prize:
        max_prize = prize
print(max_prize)

#해설답안
n = int(input())
res = 0
for i in range(n):
    tmp = input().split()
    tmp.sort()
    a, b, c = map(int,tmp)
    if a==b and b==c:
        money = 10000 + a * 1000
    elif a==b or a==c:
        money = 1000 + a * 100
    elif b==c:
        money = 1000 + b * 100
    else :
        money = c * 100
    if money > res:
        res = money
print(res)


#Chat GPT 제안 코드
n = int(input())
max_prize = 0

for _ in range(n):
    dice = sorted(map(int, input().split()))  # 정수 리스트를 정렬
    a, b, c = dice  # 언패킹하여 각 숫자에 접근
    
    if a == b == c:  # 세 숫자가 모두 같은 경우
        prize = 10000 + a * 1000
    elif a == b or b == c:  # 두 숫자만 같은 경우
        prize = 1000 + b * 100  # 정렬했으므로 중복 값은 항상 중앙에 위치
    else:  # 모두 다른 경우
        prize = c * 100  # 정렬했으므로 가장 큰 값은 마지막 요소

    max_prize = max(max_prize, prize)  # 최대 상금 업데이트

print(max_prize)