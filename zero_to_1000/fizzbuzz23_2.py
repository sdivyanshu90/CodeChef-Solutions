# Question Link: https://www.codechef.com/problems/FIZZBUZZ23_2

# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    tot = 5 * b
    print(a // tot + c)