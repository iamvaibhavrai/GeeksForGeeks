def findLongestSubsequence(a):
    n = len(a)
    temp = [1]*n

    for i in range(1,n):
        for j in range(0,i):
            if a[j] <= a[i] and temp[i] < temp[j]+1:
                temp[i] = temp[j]+1

    maximum = 1
    for i in temp:
        maximum = max(maximum,i)

    return maximum



def main():
    a = list(map(int,input().split(" ")))
    result = findLongestSubsequence(a)
    print(result)

if __name__ == '__main__':
    main()
