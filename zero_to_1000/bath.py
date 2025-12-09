# Question Link: https://www.codechef.com/problems/BATH

# cook your dish here
for _  in range(int(input())):
    x, y = map(int, input().split())
    tot = y * 2
    print(x // tot)