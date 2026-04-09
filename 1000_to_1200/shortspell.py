# cook your dish here
for _ in range(int(input())):
    a = int(input())
    l = list(map(ord, input().strip()))
    pre = l[0]
    
    for i in range(1, len(l)):
        if l[i] < pre:
            l.pop(i - 1)
            break
        pre = l[i]
    
    if a == len(l):
        l.pop()
    
    print(''.join(map(chr, l)))