from operator import truediv


def common_members(a, b):
    a_set = set(a)
    b_set = set(b)

    if len(a_set.intersection(b_set)) > 0:
        return True
    return False

if __name__ == "__main__":
    main()