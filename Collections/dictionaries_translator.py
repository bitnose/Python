

print("=== Creating a dictionary ===")
words = {}
english_word = input("Enter English word (quit ends): ")

while english_word!="quit":
    
    finnish_word = input("Enter Finnish word: ")
    words[english_word.lower()] = finnish_word.lower()
    english_word = input("Enter English word (quit ends): ")


print("\n=== Using a dictionary ===")

english_word = input("Enter English word (quit ends): ")

while english_word!="quit":

    if words.get(english_word.lower()) != None:
        print(words[english_word.lower()])
    else:
        print("Unknown word")

    english_word = input("Enter English word (quit ends): ")