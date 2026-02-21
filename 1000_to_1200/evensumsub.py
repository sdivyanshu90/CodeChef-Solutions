# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = sum(a)
    
    if total % 2 == 0:
        print(n)
    else:
        first_odd = -1
        last_odd = -1
        
        for i in range(n):
            if a[i] % 2 != 0:
                if first_odd == -1:
                    first_odd = i
                last_odd = i
        
        if first_odd == -1:
            print(0)
        else:
            print(max(n - first_odd - 1, last_odd))