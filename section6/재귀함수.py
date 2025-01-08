#나의 코드
# def decimal_to_binary(num):
#     초깃값 설정
#     binary = 0
#     n=1

#     while num > 0:
#         binary += (num % 2) * n
#         num //=2
#         n *= 10
#     print(binary)

#Chat GPT 수정 코드
# def decimal_to_binary(num, n=1, binary=0):
#     if num == 0:  # 기저 사례: num이 0이면 재귀 종료
#         print(binary)
#         return
    
#     # 현재 자리를 계산하고, n을 10배 키워서 다음 자리를 준비
#     binary += (num % 2) * n
#     decimal_to_binary(num // 2, n * 10, binary)  # 재귀 호출

# n = int(input())
# decimal_to_binary(n)

#나의 코드2 (Created 25.01.03)
# def integer_to_binary(decimal, binary_number=0, n=1):
#     #특정 조건이 호출된 경우엔 전달 받은 인자로 바로 함수 종료
#     if decimal == 0 :
#         print(binary_number)
#         return

#     #호출 됐을 때 인자를 받아서 함수 본연의 할 일을 함.
#     reminder = decimal % 2
#     binary_number = binary_number + reminder * n 
#     # n을 따로 만든 이유 
#     # #reminder가 0인 경우 10씩 곱해서 넘겨줄 수가 없다. 따라서 자릿수를 기억하는 변수 n을 만들고 10, 100, 1000을 곱해줘야 한다. 
#     # 그러면 나머지가 앞으로 쭉쭉 쌓인다.
        
#     #재귀함수 호출 
#     integer_to_binary(decimal // 2, binary_number, n*10)      #전달해줄때는 현재까지 누적된 binary_number를 해주고 해당 함수 안에서 다시 동작하도록 한다.


#해설코드
# def DFS(x):
#     if x == 0:
#         return
#     else:
#         DFS(x // 2)
#         print(x % 2, end='')

# if __name__ == "__main__":
#     n = int(input())
#     DFS(n)

# #이진트리순회(DFS)
def DFS(v):
    if v>7:
        return
    else:
        # print(v, end=" ")    #전위순회출력  --> 함수 본연의 일
        DFS(v*2)
        # print(v, end=" ")  #중위순회출력
        DFS(v*2+1)
        print(v, end=" ")  #후위순회출력

if __name__=="__main__":
    DFS(1) 
