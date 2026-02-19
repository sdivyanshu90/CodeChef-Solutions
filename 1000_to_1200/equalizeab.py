# Question Link: https://www.codechef.com/problems/EQUALIZEAB

# cook your dish here
for _ in range(int(input())):
    a, b, x = map(int, input().split())
    
    if (a + b) % 2 != 0:
        print("NO")
    elif abs(a - b) % (2 * x) != 0:
        print("NO")
    else:
        print("YES")