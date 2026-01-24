# Question Link: https://www.codechef.com/problems/FIRSTANDLAST

# cook your dish here
for _ in range(int(input())):
    N, A = int(input()), list(map(int, input().split()))
    print(max(A[0] + A[-1], max(A[i] + A[i+1] for i in range(N - 1))))