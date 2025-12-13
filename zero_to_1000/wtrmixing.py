# Question Link: https://www.codechef.com/problems/WTRMIXING

# cook your dish here
for _ in range(int(input())):
    A, B, X, Y = map(int, input().split())
    print("YES" if B>=A - Y and B <= A+X else "NO")