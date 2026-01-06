# Question Link: https://www.codechef.com/problems/BULBLIFE

# cook your dish here
for _ in range(int(input())):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(max(0, N*X - sum(A)))