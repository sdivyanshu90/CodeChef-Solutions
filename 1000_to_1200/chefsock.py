# cook your dish here
jacket, sock, total = map(int, input().split())
pairs = (total - jacket) // sock
if pairs  % 2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")