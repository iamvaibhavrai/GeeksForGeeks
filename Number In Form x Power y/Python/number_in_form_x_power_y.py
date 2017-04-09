import math

def check_num(num):
    if num == 1:
        return True
    for i in range(1,math.floor(math.sqrt(num))+1):
        for j in range(2,num):
            if i**j == num:
                return True
    return False

def main():
    num = int(input())
    if check_num(num):
        print("true")
    else:
        print("false")

if __name__ == '__main__':
    main()
