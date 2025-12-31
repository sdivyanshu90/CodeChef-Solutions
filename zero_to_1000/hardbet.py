# cook your dish here
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    mini = min(a, b, c)
    if mini == a:
        print("Draw")
    elif mini == b:
        print("Bob")
    else:
        print("Alice")