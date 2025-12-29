# cook your dish here
for _ in range(int(input())):
    n, ved, varun = map(int, input().split())
    a = list(map(int, input().split()))
    final_height_ved = ved + max(a)
    final_height_varun = varun + (sum(a) - max(a))
    if final_height_ved > final_height_varun:
        print("Ved")
    elif final_height_varun > final_height_ved:
        print("Varun")
    else:
        print("Equal")