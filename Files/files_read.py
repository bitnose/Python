from pathlib import Path

filename = input("Enter file name: ")

try:
    path = Path(__file__).resolve().parent
    path = path / filename
    contents = path.read_text(encoding="UTF-8") 
    print(contents)
    
except FileNotFoundError:
    print(f"The file {filename} is not found")
