# Question Link: https://www.codechef.com/problems/CABLE

# cook your dish here
a, b, c, x = map(int, input().split())
cuboid = a * b * c
cube = x ** 3
if cuboid > cube:
    print("Cuboid")
else:
    print("Cube")