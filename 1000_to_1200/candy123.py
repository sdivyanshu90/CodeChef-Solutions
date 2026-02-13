# cook your dish here
for _ in range(int(input())):
    A, B = map(int, input().split())
    
    limak = 0
    bob = 0
    turn = 1
    
    while True:
        if turn % 2 == 1:
            if limak + turn > A:
                print("Bob")
                break
            limak += turn
        else:
            if bob + turn > B:
                print("Limak")
                break
            bob += turn
        
        turn += 1