# Question Link: https://www.codechef.com/problems/MAXCOIN

# cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    
    gain = (2 ** (n + 1)) - (2 ** (n - x + 1))
    loss = (2 ** (n - x + 1)) - 2
    
    print(gain - loss)