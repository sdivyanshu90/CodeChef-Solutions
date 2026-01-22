# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    f_x = x ** 4
    t_y = y ** 2
    t_x = x ** 2
    eq1 = f_x + 4*t_y
    eq2 = 4 * t_x * y
    if eq1 == eq2:
        print("YES")
    else:
        print("NO")