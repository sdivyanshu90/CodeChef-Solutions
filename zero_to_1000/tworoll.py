# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    steps = []
    for i in range(6):
        steps.append(y + i)
        
    set_step = set()
    for d1 in steps:
        for d2 in steps:
            set_step.add(d1 + d2)
        
    if 50 - x in set_step:
        print("Yes")
    else:
        print("No")