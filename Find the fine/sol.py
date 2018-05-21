#code
for _ in range(int(input())):
    n,date = map(int,input().split())
    car = list(map(int,input().split()))
    fine = list(map(int,input().split()))
    total_fine = 0
    check = date%2
    for i in range(n):
        if car[i]%2 != check:
            total_fine += fine[i]
    print(total_fine)
