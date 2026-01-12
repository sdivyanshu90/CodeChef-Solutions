# cook your dish here
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    first = a[0]
    count = 1
    for i in range(1, n):
        if first != a[i]:
            count+=1
            
            if count == 2:
                print(2)
                break
            
        first = a[i]
        
    else:
        print(-1)