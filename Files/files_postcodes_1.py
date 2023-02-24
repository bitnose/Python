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

    filename = input("Enter postcode file name: ")
    data = load_data(filename) 

    if data != None:
        print(f"\n{len(data)} rows")

        postcode = input("\nEnter postcode: ")

        if data.get(postcode) != None:
            print(f"\n{postcode} {data[postcode][0]}")
            print(f"{postcode} {data[postcode][1]}")
        else:
            print("Unknown postcode")

    else:
        print(f"\nThe file {filename} is not found")


       

if __name__ == "__main__":
    main()