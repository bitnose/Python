def make_box(a: str):
    length = len(a.strip()) + 4
    print(length * "-")
    print(f"| {a.strip()} |")
    print(length * "-")

def main():
    try:
        make_box(str(input("Enter a string: ")))
    except ValueError:
        print("Value is not a string.")

main()

