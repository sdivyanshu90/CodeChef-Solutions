# Question Link: https://www.codechef.com/problems/GOODSUB7

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 0:
        print(0)
        continue
    
    count = 1
    last_parity = a[0] % 2
    
    for i in range(1, n):
        current_parity = a[i] % 2
        if current_parity != last_parity:
            count += 1
            last_parity = current_parity
            
    print(count)