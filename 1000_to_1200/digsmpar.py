# cook your dish here
for _ in range(int(input())):
    n = input().strip()
    
    def digit_sum(x):
        return sum(int(d) for d in x)
    
    original_parity = digit_sum(n) % 2
    x = int(n) + 1
    
    while digit_sum(str(x)) % 2 == original_parity:
        x += 1
    
    print(x)