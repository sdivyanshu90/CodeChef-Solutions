# Question Link: https://www.codechef.com/problems/BUILDINGRACE

# cook your dish here
for _ in range(int(input())):
    chef_floor, chefina_floor, chef_speed, chefina_speed = map(int, input().split())
    chef_min = chef_floor / chef_speed
    chefina_min = chefina_floor / chefina_speed
    if chef_min > chefina_min:
        print("Chefina")
    elif chefina_min > chef_min:
        print("Chef")
    else:
        print("Both")