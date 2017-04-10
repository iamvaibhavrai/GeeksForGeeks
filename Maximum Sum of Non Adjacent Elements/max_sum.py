def main():
    a = [2,5,5,6,5]
    including = a[0]
    excluding = 0
    for i in range(1,len(a)):
        new_excluding = max(including,excluding)
        including = a[i] + excluding
        excluding = new_excluding
    print(max(including,excluding))

if __name__ == '__main__':
    main()
