#code
for _ in range(int(input())):
    x = input()
    if len(x) == 1:
        print(x)
    else:
        res = int(x[0])
        for i in range(1,len(x),2):
            if x[i] == 'A':
                res = res & int(x[i+1])
            elif x[i] == 'B':
                res = res | int(x[i+1])
            else:
                res = res ^ int(x[i+1])
    print(res)
