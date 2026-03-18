# cook your dish here
for _ in range(int(input())):
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    
    if c >= sum(arr):
        print("Yes")
    else:
        print("No")