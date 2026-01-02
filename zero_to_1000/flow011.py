# cook your dish here
for _ in range(int(input())):
    salary = int(input())
    if salary < 1500:
        print(salary * 2)
    else:
        print(salary + (salary * 0.98) + 500)