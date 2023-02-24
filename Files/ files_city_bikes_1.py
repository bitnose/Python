from pathlib import Path
from datetime import datetime

# Read the csv file
def load_file(filename):

    try:
        path = Path(__file__).resolve().parent
        path = path / filename
        contents = path.read_text(encoding="UTF-8") 

        lines = contents.splitlines()
        lines.pop(0)
        
        return lines

    except FileNotFoundError:
        return None

def show_statistics(lines):

    kilometers = 0
    rides = 0
    sum_duration_s = 0

    for line in lines:
        fields = line.split(",")

        kilometers += int(fields[6])/1000
        rides += 1

        # 2021-06-30T23:57:41

        departDate = datetime.strptime(fields[0], '%Y-%m-%dT%H:%M:%S')
        arriveDate = datetime.strptime(fields[1], '%Y-%m-%dT%H:%M:%S')

        duration = arriveDate - departDate
        sum_duration_s += float(duration.seconds)

    
    avg_distance = int(kilometers)/rides
    avg_duration = int(sum_duration_s/rides/60)

    print(f"\n{int(kilometers)} kilometers on {rides} bike rides")
    print(f"Average distance: {avg_distance:.1f} kilometers")
    print(f"Average duration: {avg_duration} minutes")

def main():

    filename = input("Enter file name: ")
    try: 
        path = Path(__file__).resolve().parent
        path = path / filename

        if path.is_file():
            lines = load_file(filename)
            show_statistics(lines)
        else:
            print(f"\nThe file {filename} is not found")

    except FileNotFoundError:
        print(f"The file {filename} is not found")
        

if __name__ == "__main__":
    main()