# Question Link: https://www.codechef.com/problems/PPSUM

# cook your dish here
for _ in range(int(input())):
    d, n = map(int, input().split())
    current = n

    for _ in range(d):
        current = current * (current + 1) // 2

    print(current)