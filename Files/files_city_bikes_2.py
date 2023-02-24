from pathlib import Path
from datetime import datetime

def load_file(filename):

    try:
        path = Path(__file__).resolve().parent
        path = path / filename
        contents = path.read_text(encoding="UTF-8") 

        lines = contents.splitlines()
        lines.pop(0)

        data = lines
        
        return data

    except FileNotFoundError:
        return None

def show_statistics(data):

    kilometers = 0
    rides = 0
    sum_duration_s = 0

    for line in data:
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


def show_max_departures(data):

    # names of those bike stations who have the highest number of departures, ascending
    print("Maximum number of departures from a bike station:")

    station = None
    max_departures = {}

    for line in data:
        fields = line.split(",")
        station = fields[2]

    

    

    


def main():

    filename = input("Enter file name: ") 
    path = Path(__file__).resolve().parent
    path = path / filename

    if path.is_file():
        lines = load_file(filename)
        show_statistics(lines)
    else:
        print(f"\nThe file {filename} is not found")

if __name__ == "__main__":
    main()