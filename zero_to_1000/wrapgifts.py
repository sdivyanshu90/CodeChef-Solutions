# Question Link: https://www.codechef.com/problems/WRAPGIFTS

# cook your dish here
for _ in range(int(input())):
    h, l, w = map(int, input().split())
    surface_area = 2 * (h * l + l * w + w * h)
    print(1000 // surface_area)