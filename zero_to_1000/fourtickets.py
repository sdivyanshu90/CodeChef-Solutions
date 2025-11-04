# Question Link: https://www.codechef.com/problems/FOURTICKETS

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n * 4 <= 1000:
        print("YES")
    else:
        print("NO")