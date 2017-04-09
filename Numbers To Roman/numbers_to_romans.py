conversions_dict = {
1:"I",
4:"IV",
5:"V",
9:"IX",
10:"X",
40:"XL",
50:"L",
90:"XC",
100:"C",
400:"CD",
500:"D",
900:"CM",
1000:"M"
}
conversion_list = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

result = []

def convertToRoman(quo,i):
    global result
    result.append(conversions_dict[i]*quo)

def listToString(result):
    return ''.join(result)

def main():
    num = int(input())
    rem = num
    while rem!=0:
        for i in conversion_list:
            if i <= rem:
                break
        quo = rem//i
        rem = rem%i
        convertToRoman(quo,i)
    print(listToString(result))

if __name__ == '__main__':
    main()
