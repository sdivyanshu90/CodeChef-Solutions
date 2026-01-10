# Question Link: https://www.codechef.com/problems/ALTERADD

# cook your dish here
for _ in range(int(input())):
    a, b = map(int, input().split())
    
    diff = b - a
    if diff % 3 == 2:
        print("NO")
    else:
        print("YES")