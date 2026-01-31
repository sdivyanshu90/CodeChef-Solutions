# cook your dish here
for _ in range(int(input())):
    s = input()
    count = 0
    res = 0
    for char in s:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1
        else:
            count = 0
        res = max(res, count)
    if res > 2:
        print("Happy")
    else:
        print("Sad")