# cook your dish here
p = list(map(int, input().split()))

res = 0
for num in p:
    if num >= 10:
        res += 1
        
print(res)