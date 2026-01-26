# cook your dish here
for _ in range(int(input())):
    n, k, x = map(int, input().split())
    print(abs((n - k) % x - k % x))