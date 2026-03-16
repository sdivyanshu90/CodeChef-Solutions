# Question Link: https://www.codechef.com/problems/CIELAB

# cook your dish here
a, b = map(int, input().split())
diff = a - b

if diff % 10 == 9:
    print(diff - 1)
else:
    print(diff + 1)