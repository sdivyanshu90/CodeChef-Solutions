# Question Link: https://www.codechef.com/problems/PIZZAPARTY

# cook your dish here
boy, girl = map(int, input().split())
tot = (boy + 1) * 4 + (girl * 3)
if tot % 8 == 0:
    print(tot // 8)
else:
    print(tot // 8 + 1)

# Approach 2: Using math.ceil
# import math
# boy, girl = map(int, input().split())
# tot = (boy + 1) * 4 + (girl * 3)
# print(math.ceil(tot / 8))
# Approach 3: Using integer arithmetic
# boy, girl = map(int, input().split())
# tot = (boy + 1) * 4 + (girl * 3)
# print((tot + 7) // 8)