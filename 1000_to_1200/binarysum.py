# cook your dish here
import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    half_ceil, half_floor = math.ceil(n / 2), math.floor(n / 2)
    if half_floor == k or half_ceil == k:
        # print(f"n: {n}, half_floor: {half_floor}, half_ceil: {half_ceil}")
        print("YES")
    else:
        print("NO")
        # print(f"n: {n}, half_floor: {half_floor}, half_ceil: {half_ceil}")