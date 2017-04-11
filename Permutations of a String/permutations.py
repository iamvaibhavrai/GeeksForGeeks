def listToString(string):
    string = ''.join(string)
    return string

def printPermutations(string,l,r):
    if l == r:
        print(listToString(string))
    for i in range(l,r):
        string[i],string[l] = string[l],string[i]
        printPermutations(string,l+1,r)
        string[i],string[l] = string[l],string[i]


def main():
    string = list(input())
    printPermutations(string,0,len(string))

if __name__ == '__main__':
    main()
