def new_doubled_list(list):
    doubled_list = []
    for item in range(len(list)):
        doubled_list.append(list[item] * 2)

    return doubled_list

def main():
    first_list = [1, 2, 3, 4, 5, 6]
    second_list = new_doubled_list(first_list)
    print(first_list)
    print(second_list)
main()