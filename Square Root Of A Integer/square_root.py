def findSquareRoot(num,start,end):
    if num == 1:
        print("1")
        return
    if start == end:
        print(start-1)
        return
    mid = (start + end)//2
    if mid**2 == num:
        print(mid)
        return
    elif mid**2 <num:
        findSquareRoot(num,mid+1,end)
    else:
        findSquareRoot(num,start,mid)

def main():
    num = int(input())
    findSquareRoot(num,0,num)

if __name__ == '__main__':
    main()
