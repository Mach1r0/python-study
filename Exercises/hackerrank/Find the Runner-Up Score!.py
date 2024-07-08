if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    arr = list(set(arr)) # remove the duplicate lines
    arr.sort()
    print(arr[-2])