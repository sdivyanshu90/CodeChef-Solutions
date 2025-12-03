# cook your dish here
n = int(input())
a = list(map(int, input().split()))

odd, even = 0, 0
for num in a:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
        
if even > odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")