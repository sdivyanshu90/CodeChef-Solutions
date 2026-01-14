# cook your dish here
import math

for _ in range(int(input())):
    n = int(input())
    count = 0
    while n > 0:
        n //= 5
        count += n
    print(count)