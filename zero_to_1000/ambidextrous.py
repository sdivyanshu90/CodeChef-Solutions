# cook your dish here
import math

for _ in range(int(input())):
    l, r, m = map(int, input().split())
    code = m // r
    page = math.ceil(m / l)
    print(code + page)