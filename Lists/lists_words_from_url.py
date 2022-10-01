from urllib.request import urlopen

url = "https://www.mit.edu/~ecprice/wordlist.10000" 
word_list = urlopen(url).read().splitlines()
counters = [0] * 23
letters = 0
sum = len(word_list)

for i in range(sum):
    
    word = word_list[i] 
    word_count = len(word)
    num = counters[word_count]
    lenght=len(counters)

    if word_count<lenght:
        counters[word_count] += 1 
        letters = letters + word_count

average = float(letters / sum)

print(f"{sum} words")
print(f"The average word length is {average:.3f}")
print("Length Count")

for i in range(len(counters)): 
    if i>0:
        print(f"{i:6d} {counters[i]:5d}")

