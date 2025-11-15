# Question Link: https://www.codechef.com/problems/HS08TEST

# cook your dish here
x, y = map(float, input().split())
x = int(x)
y = float(y)
if x % 5 == 0 and y >= x + 0.50:
    y -= (x + 0.50)
print(f"{y:.2f}")