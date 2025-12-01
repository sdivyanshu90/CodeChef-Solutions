# Question Link: https://www.codechef.com/problems/EXAMCHEF

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    perc = (x * y) * 0.5
    # print(perc)
    if perc < z:
        print("YES")
    else:
        print("NO")