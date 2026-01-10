# Question Link: https://www.codechef.com/problems/CONN

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n < 8:
        if n % 2 == 0 or n == 7:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")