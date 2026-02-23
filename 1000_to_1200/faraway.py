# Question: https://www.codechef.com/problems/FARAWAY

# cook your dish here
for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    summ , maxi = 0, 0
    for i in range(N):
        if A[i] > M // 2:
            maxi = abs(A[i] - 1)
        else:
            maxi = abs(A[i] - M)
        
        summ = summ + maxi
        maxi = 0
    print(summ)