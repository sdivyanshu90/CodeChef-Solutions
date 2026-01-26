# cook your dish here
for _ in range(int(input())):
    N, M = map(int, input().split())
    S = input()
    
    alice = S.count("1")
    bob = S.count("0")
    remaining_matches = N - M
    diff = abs(alice - bob)
    
    if diff <= remaining_matches and (remaining_matches - diff) % 2 == 0:
        print("Yes")
    else:
        print("No")