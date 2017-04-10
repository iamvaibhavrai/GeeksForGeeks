def main():
    a = [1,2,1,3,3,2,3]
    xor = a[0]
    print(xor)
    for i in range(1,len(a)):
        xor ^= a[i]
    print(xor)

if __name__ == '__main__':
    main()
