# cook your dish here
for _ in range(int(input())):
    x, y, p, q = map(int, input().split())
    # print(f"x: {x}, y: {y}, p: {p}, q: {q}")
    chef_time = x + 10 * p
    chefina_time = y + 10 * q
    # print(f"Chef time: {chef_time}, Chefina time: {chefina_time}")
    if chef_time > chefina_time:
        print("Chefina")
    elif chefina_time > chef_time:
        print("Chef")
    else:
        print("Draw")