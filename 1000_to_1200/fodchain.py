# cook your dish here
for _ in range(int(input())):
    e, k = map(int, input().split())
    count = 1
    while e >= k:
        e = e // k
        count += 1
    print(count)