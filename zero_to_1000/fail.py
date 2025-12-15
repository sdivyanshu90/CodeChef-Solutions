# cook your dish here
for _ in range(int(input())):
    n = int(input())
    avg = 40
    a = list(map(int, input().split()))
    flag = True
    total = 0
    for i in range(1, len(a)+1):
        total += a[i - 1]
        run_avg = total / i
        if run_avg < avg:
            flag = False
            break
            
    if flag:
        print("Yes")
    else:
        print("No")