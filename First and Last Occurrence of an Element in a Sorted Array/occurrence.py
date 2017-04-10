def main():
    a = [1,2,4,5,5,5,5,5,5,5]
    x = 5
    startFlag,endFlag = 0,len(a)-1
    for i in range(len(a)):
        if startFlag != 0 and endFlag != 0:
            break
        if a[i] == x and startFlag == 0:
            startFlag = i
        if a[i] > x:
            endFlag = i-1

    print("First Occurence: ",startFlag)
    print("Last Occurence: ",endFlag)

if __name__ == '__main__':
    main()
