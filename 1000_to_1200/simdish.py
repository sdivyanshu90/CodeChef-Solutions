# cook your dish here
for _ in range(int(input())):
    a = list(map(str, input().split()))
    b = list(map(str, input().split()))
    
    count = 0
    for i in range(len(a)):
        if a[i] in b:
            count += 1
            
    if count >= 2:
        print("similar")
    else:
        print("dissimilar")