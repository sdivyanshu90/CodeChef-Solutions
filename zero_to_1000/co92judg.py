# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.remove(max(a))
    b.remove(max(b))
    suma = sum(a)
    sumb = sum(b)
    if suma < sumb:
        print("Alice")
    elif sumb < suma:
        print("Bob")
    else:
        print("Draw")