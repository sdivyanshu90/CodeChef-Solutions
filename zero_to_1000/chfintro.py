# Question Link: https://www.codechef.com/problems/CHFINTRO

# cook your dish here
n, r = map(int, input().split())
for _ in range(n):
    x = int(input())
    if x >= r:
        print("Good boi")
    else:
        print("Bad boi")