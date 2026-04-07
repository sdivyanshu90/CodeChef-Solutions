# Question Link: https://www.codechef.com/problems/ANKTRAIN

# cook your dish here
partners = {1: 'LB', 4: 'LB', 2: 'MB', 5: 'MB', 3: 'UB', 6: 'UB', 7: 'SL', 0: 'SU'}

for _ in range(int(input())):
    n = int(input())
    remainder = n % 8

    if remainder in {1, 2, 3}:
        print(f"{n + 3}{partners[remainder]}")
    elif remainder in {4, 5, 6}:
        print(f"{n - 3}{partners[remainder]}")
    elif remainder == 7:
        print(f"{n + 1}{partners[0]}")
    else:
        print(f"{n - 1}{partners[7]}")