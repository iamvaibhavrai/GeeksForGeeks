def equilibriumIndex(a,n):
    s = 0
    for i in a:
        s+=i
    temp = 0
    for i in range(len(a)):
        if temp == (s-a[i]-temp):
            print(i)
        temp += a[i]

def main():
    a = [-7,1,5,2,-4,3,0]
    equilibriumIndex(a,len(a))

if __name__ == '__main__':
    main()
