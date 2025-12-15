# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    largest_so_far = a[0]
    res = []
    for num in a:
        if num >= largest_so_far:
            largest_so_far = num
            res.append(1)
        else:
            res.append(0)
            
    print(" ".join(map(str, res)))