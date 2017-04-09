a = [4,3,7,8,6,2,1]
for i in range(1,len(a)):
    if i%2 == 0:
        if a[i-1] < a[i]:
            a[i-1],a[i] = a[i],a[i-1]
    else:
        if a[i-1] > a[i]:
            a[i-1],a[i] = a[i],a[i-1]
print(a)
