def main():
    s = list(input())
    temp_char = s[0]
    counter = 0
    result = [temp_char]
    for i in s:
        if i == temp_char:
            counter += 1
        else:
            result.append(str(counter))
            result.append(i)
            temp_char = i
            counter = 1
    result.append(str(counter))
    print(''.join(result))


if __name__ == '__main__':
    main()
