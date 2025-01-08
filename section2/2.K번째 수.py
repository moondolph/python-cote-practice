'''
Project ID : Coding test Practice
Program ID : Output the k-th smallest number from a specified subrange of N numbers after sorting.
Purpose : Retrieve the k-th smallest number from the s-th to e-th position in a sorted subrange of numbers.
Revision History:
    created November 5th in 2024 by Juyong Sim
'''


#My code
T = int(input())
for i in range(1,T+1):
    N,s,e,k = map(int,input().split())
    a=list(map(int,input().split()))   # a = [map(int,input().split())] is also possible
    a = a[s-1:e]
    a.sort()
    print(f"#{i} {a[k-1]}")


#Answer code
T=int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int,input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))


# formatting 
    # Way 1 : Previous Python3
        # print("#%i %i" %(i+1,a[k-1]))
    # Way 2 : Next Python3 
        # print("#{} {}".format(i+1,a[k-1]))  
    # Way 3 : Next Python 3.6 
        # print(f"#{i+1} {a[k-1]}")