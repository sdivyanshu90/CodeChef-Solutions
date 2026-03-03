# Question Link: https://www.codechef.com/problems/TRAVELPS

# cook your dish here
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    s = input()
    zeros, ones = 0, 0
    for num in s:
        if num == "0":
            zeros += 1
        else:
            ones += 1
            
    print(zeros * a + ones * b)