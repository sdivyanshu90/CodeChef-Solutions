# cook your dish here
for _ in range(int(input())):
    n, left, x = map(int, input().split())
    right = n - left
    mini = min(left, right)
    print(x * mini)