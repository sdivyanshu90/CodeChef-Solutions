# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    count = 0
    for num in a:
        if num == 0:
            count += 1
            
    if count >= 2:
        print("Water filling time")
    else:
        print("Not now")