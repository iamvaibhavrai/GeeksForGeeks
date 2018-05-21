#code
for _ in range(int(input())):
    n = int(input())
    x = list(map(int,input().split()))
    count = 0
    for i in range(n-1):
        if x[i] == 0:
            count += 1
        elif x[i] == x[i+1]:
            x[i] *= 2
            x[i+1] = 0
            count += 1
    i =  0
    temp = count
    while count > 0 and i < len(x):
        if x[i] == 0:
            del x[i]
            count -= 1
        else:
            i += 1
    for i in range(temp):
        x.append(0)
    for i in range(n):
        print(x[i], end=" ")
    print()
