# Question Link: https://www.codechef.com/problems/CARDGAME1

# cook your dish here
res = []
for _ in range(int(input())):
    n , x = map(int, input().split())
    even_count = n // 2
    odd_count = n - even_count
    
    if x % 2 == 0:
        temp = even_count - 1
    else:
        temp = odd_count - 1
    res.append(temp)
print(*res, sep='\n')