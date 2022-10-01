def remove_successive_duplicates(a):
    try:
        for i in range(len(a)):
            index = i + 1
            while a[i] == a[index]:
                del a[index]
            i += 1
        return a
    except:
        return a


def main():
    a = [1, 1, 1, 2, 1, 2, 2, 2, 3, 3, 3]
    b = [1]
    c = [3, 1, 1, 2, 1, 2, 2, 2, 3]
    remove_successive_duplicates(c)
    print(c)

if __name__ == "__main__":
    main()
