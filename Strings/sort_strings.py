def make_key(s: str) -> str:
    key = list(s)
    for i in range(0, len(key)):
        key[i] = key[i].lower()
        if key[i] == "ä":
            key[i] = "å"
        elif key[i] == "å":
            key[i] = "ä"
    return key
def main():
    strings = ["ä", "å", "Ö", "By", "bag"]
    print(sorted(strings)) 
    ['By', 'bag', 'Ö', 'ä', 'å'] 
    print(sorted(strings, key=make_key)) 
    ['bag', 'By', 'å', 'ä', 'Ö']
main()