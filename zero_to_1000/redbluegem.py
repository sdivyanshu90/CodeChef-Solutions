# cook your dish here
r, b, p, q = map(int, input().split())
red_gem = r * p
blue_gem = b * q
if red_gem > blue_gem:
    print(red_gem)
else:
    print(blue_gem)