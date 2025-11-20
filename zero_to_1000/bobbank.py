# Question Link: https://www.codechef.com/problems/BOBBANK

# cook your dish here
for _ in range(int(input())):
    w, x, y, z = map(int, input().split())
    gain = x - y
    print(w + gain * z)