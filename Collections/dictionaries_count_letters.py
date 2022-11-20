from urllib.request import urlopen

# Fetch the content of a text from the given URL and save it as single a string.
# Then the program should count the letters in the string and display the result as shown in the example output below.
#you should use a dictionary to hold the count of occurrences of each distinct letter in the string
#you should count letters in a case-insensitive way
#you should not display a letter if it does not appear in the string.

url = "https://www.mit.edu/~ecprice/wordlist.10000" 
content = urlopen(url).read().decode("UTF-8")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
count = 0
d = {}

for letter in letters:

     d[letter] = content.count(letter) + content.count(letter.upper())
     if d[letter] != 0:
        print(f"{letter:8s} {d[letter]}")
