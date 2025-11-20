# Question Link: https://www.codechef.com/problems/ASSIGNMNT

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    tot = x * y
    day_to_min = z * 24 * 60
    if tot <= day_to_min:
        print("YES")
    else:
        print("NO")