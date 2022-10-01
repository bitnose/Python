word = input("Enter a word (quit ends): ")
words = []

while word != "quit":
    words.append(word)
    word = input("Enter a word (quit ends): ")
    
words.sort()
print(*words, sep="\n")
