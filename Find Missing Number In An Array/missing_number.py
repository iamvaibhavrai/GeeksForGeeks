def main():
    a = [1,4,2,5,6,7]
    l = len(a)+1
    s = (l*(l+1))//2
    for i in a:
        s = s-i
    print(s)

if __name__ == '__main__':
    main()
