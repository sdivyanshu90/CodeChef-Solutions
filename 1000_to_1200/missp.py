# cook your dish here
for _ in range(int(input())):
    n = int(input())
    dolls = []
    for _ in range(n):
        t = int(input())
        dolls.append(t)
        
    # print(dolls)
    for types in dolls:
        if dolls.count(types) % 2 == 1:
            print(types)
            break