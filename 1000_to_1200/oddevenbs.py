# Question Link: https://www.codechef.com/problems/ODDEVENBS

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    
    if (n - sum(b)) % 2 == 0:
        print("YES")
    else:
        print("NO")