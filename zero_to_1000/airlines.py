# Question Link: https://www.codechef.com/problems/AIRLINES

# cook your dish here
for _ in range(int(input())):
    x, y, z = map(int, input().split())
    total_seat = x * 10
    # print(f"Total Seat: {total_seat}")
    if total_seat > y:
        print(y * z)
    else:
        print(total_seat * z)