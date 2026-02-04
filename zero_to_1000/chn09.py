# Question Link: https://www.codechef.com/problems/CHN09

# cook your dish here
for _ in range(int(input())):
    s = input()
    a = s.count("a")
    b = s.count("b")
    print(min(a, b))