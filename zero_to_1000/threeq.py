# cook your dish here
for _ in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    zeroa, onea = 0, 0
    zerob, oneb = 0, 0
    for num in a:
        if num == 1:
            onea += 1
        else:
            zeroa += 1
    for num in b:
        if num == 1:
            oneb += 1
        else:
            zerob += 1
    
    if onea == oneb or zeroa == zerob:
        print("Pass")
    else:
        print("Fail")