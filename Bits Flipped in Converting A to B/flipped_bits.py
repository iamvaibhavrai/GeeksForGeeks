def convert(a,b):
    c = a ^ b
    counter = 0
    while(c!=0):
        if c&1 == 1:
            counter+=1
        c >>= 1
    return counter

def main():
    a = int(input())
    b = int(input())
    print(convert(a,b))

if __name__ == '__main__':
    main()
      
