# Question Link: https://www.codechef.com/problems/HELIUM3

# cook your dish here
for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    tot_power = a * b
    moon_power = x * y
    if moon_power >= tot_power:
        print("Yes")
    else:
        print("No")