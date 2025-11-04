# Question Link: https://www.codechef.com/problems/MVR

# cook your dish here
a, b, x, y = map(int, input().split())
messi = 2 * a + b
ronaldo = 2 * x + y
if messi == ronaldo:
    print("Equal")
elif messi > ronaldo:
    print("Messi")
else:
    print("Ronaldo")