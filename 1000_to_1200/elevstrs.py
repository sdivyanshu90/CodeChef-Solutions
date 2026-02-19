# cook your dish here
import math

for _ in range(int(input())):
    n, stairs_velocity, elevator_velocity = map(int, input().split())
    if (stairs_velocity * math.sqrt(2)) > elevator_velocity:
        print("Stairs")
    else:
        print("Elevator")