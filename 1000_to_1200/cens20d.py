# Question Link: https://www.codechef.com/problems/CENS20D

# cook your dish here
from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    count = 0
    bit_count = defaultdict(int)

    for num in arr:
        for key in list(bit_count):
            if num & key == key:
                count += bit_count[key]
        bit_count[num] += 1
    
    print(count)