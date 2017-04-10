def printTypeOfArray(a):
    types = {
    2:"Ascending",
    1:"Descending",
    21:"Ascending rotated",
    12:"Descending rotated"
    }
    f_arr,f_asc,f_des,maximum = [],0,0,a[0]
    for i in range(1,len(a)):
        if a[i] > a[i-1]:
            maximum = a[i] if a[i] > maximum else maximum
            if f_asc != 1:
                f_arr.append("2")
            f_asc = 1
        if a[i] < a[i-1]:
            if f_des != 1:
                f_arr.append("1")
            f_des = 1

    f_arr = ''.join(f_arr)
    print(types[int(f_arr)],"with maximum element",maximum)

def main():
    asc = [2,4,6,8,9]
    des = [10,7,5,4,3]
    rotated_asc = [6,8,11,2,4]
    rotated_des = [5,4,3,12,7]
    printTypeOfArray(asc)
    printTypeOfArray(des)
    printTypeOfArray(rotated_asc)
    printTypeOfArray(rotated_des)

if __name__ == '__main__':
    main()
