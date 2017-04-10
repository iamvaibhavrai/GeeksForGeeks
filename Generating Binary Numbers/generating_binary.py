from queue import Queue
def main():
    n = int(input())
    q = Queue()
    q.put("1")
    print("1")
    while n>1:
        x = q.get()
        x0 = x+"0"
        x1 = x+"1"
        print(x0)
        q.put(x0)
        n -= 1
        if n>0:
            print(x1)
            q.put(x1)
        n -= 1

if __name__ == '__main__':
    main()
