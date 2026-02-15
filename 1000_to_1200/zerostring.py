# Question Link: https://www.codechef.com/problems/ZEROSTRING

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    ones = s.count("1")
    print(min(ones, 1 + (n - ones)))