from pathlib import Path

def load_data(filename):

    try:
        path = Path(__file__).resolve().parent
        path = path / filename
        contents = path.read_text(encoding="UTF-8") 

        lines = contents.splitlines()
        dict = {}

        for line in lines: 
            fields = line.split(";")
            dict[fields[0]] = (fields[1], fields[2])    
    
        data = dict
        return data

    except FileNotFoundError:
        return None


def main():

   # filename = input("Enter postcode file name: ")
    filename = "postcodes.csv"
    data = load_data(filename) 

    if data != None:

        place = input("\nEnter place name: ").upper()
        print()

        found = False

        for key, value in data.items():
            if value[0] == place or value[1] == place: 
                found = True
                print(f"{key} {place}")

        if not found:
            print("No postoffice found")

    else:
        print(f"\nThe file {filename} is not found")


if __name__ == "__main__":
    main()